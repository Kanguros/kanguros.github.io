# ruff: noqa: TRY401

import csv
import logging
import sys
from typing import Any

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication


def setup_connection(organization_url: str, pat: str) -> Connection:
    """
    Create a connection to Azure DevOps.
    """
    credentials = BasicAuthentication("", pat)
    return Connection(base_url=organization_url, creds=credentials)


def get_matching_repositories(
    connection: Connection, project: str, prefixes: list[str]
) -> list[dict[str, Any]]:
    """
    Get repositories that match the given prefixes.
    """
    git_client = connection.clients.get_git_client()
    repositories = git_client.get_repositories(project)

    matching_repos = []
    for repo in repositories:
        for prefix in prefixes:
            if repo.name.startswith(prefix):
                matching_repos.append(
                    {"id": repo.id, "name": repo.name, "url": repo.url}
                )
                break

    return matching_repos


def get_repository_builds(
    connection: Connection, project: str, repository_id: str
) -> list[dict[str, Any]]:
    """
    Get builds for a repository.
    """
    build_client = connection.clients.get_build_client()
    builds = build_client.get_builds(project, repository_id=repository_id)

    build_list = []
    for build in builds:
        build_list.append(
            {
                "id": build.id,
                "number": build.build_number,
                "status": build.status,
                "result": build.result,
                "url": build.url,
            }
        )

    return build_list


def get_repository_pipelines(
    connection: Connection, project: str, repository_id: str
) -> list[dict[str, Any]]:
    """
    Get pipelines for a repository.
    """
    release_client = connection.clients.get_release_client()
    definitions = release_client.get_release_definitions(
        project, artifact_source_id=repository_id
    )

    pipeline_list = []
    for definition in definitions:
        pipeline_list.append(
            {
                "id": definition.id,
                "name": definition.name,
                "url": definition.url,
            }
        )

    return pipeline_list


def process_repository(
    connection: Connection, project: str, repo: dict[str, Any]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """
    Process a single repository to get its builds and pipelines.
    """
    repo_id = repo["id"]
    repo_name = repo["name"]
    logging.info(f"Processing repository: {repo_name}")

    builds = []
    try:
        builds = get_repository_builds(connection, project, repo_id)
        logging.info(f"Found {len(builds)} builds for repository {repo_name}.")
    except Exception as e:
        logging.exception(
            f"Error retrieving builds for repository {repo_name}: {str(e)}"
        )

    pipelines = []
    try:
        pipelines = get_repository_pipelines(connection, project, repo_id)
        logging.info(
            f"Found {len(pipelines)} pipelines for repository {repo_name}."
        )
    except Exception as e:
        logging.exception(
            f"Error retrieving pipelines for repository {repo_name}: {str(e)}"
        )

    return builds, pipelines


def create_base_record(repo: dict[str, Any]) -> dict[str, Any]:
    """
    Create a base record with repository information.
    """
    return {
        "repository_id": repo["id"],
        "repository_name": repo["name"],
        "repository_url": repo["url"],
        "build_id": "",
        "build_number": "",
        "build_status": "",
        "build_result": "",
        "build_url": "",
        "pipeline_id": "",
        "pipeline_name": "",
        "pipeline_url": "",
    }


def flatten_repository_with_builds(
    repo: dict[str, Any], builds: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """
    Flatten repository data with its builds.
    """
    flattened_data = []

    for build in builds:
        record = create_base_record(repo)
        record.update(
            {
                "build_id": build["id"],
                "build_number": build["number"],
                "build_status": build["status"],
                "build_result": build["result"],
                "build_url": build["url"],
            }
        )
        flattened_data.append(record)

    return flattened_data


def flatten_repository_with_pipelines(
    repo: dict[str, Any], pipelines: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """
    Flatten repository data with its pipelines.
    """
    flattened_data = []

    for pipeline in pipelines:
        record = create_base_record(repo)
        record.update(
            {
                "pipeline_id": pipeline["id"],
                "pipeline_name": pipeline["name"],
                "pipeline_url": pipeline["url"],
            }
        )
        flattened_data.append(record)

    return flattened_data


def flatten_data(
    repositories: list[dict[str, Any]],
    builds_data: list[list[dict[str, Any]]],
    pipelines_data: list[list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    """
    Flatten the data for CSV storage.
    """
    flat_data = []

    for i, repo in enumerate(repositories):
        builds = builds_data[i]
        pipelines = pipelines_data[i]

        # If no builds or pipelines, add just the repo info
        if not builds and not pipelines:
            flat_data.append(create_base_record(repo))

        # Add entries for each build
        flat_data.extend(flatten_repository_with_builds(repo, builds))

        # Add entries for each pipeline
        flat_data.extend(flatten_repository_with_pipelines(repo, pipelines))

    return flat_data


def save_to_csv(data: list[dict[str, Any]], file_path: str) -> None:
    """
    Save flat data to a CSV file.
    """
    if not data:
        logging.warning("No data to save.")
        return

    field_names = data[0].keys()

    with open(file_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

    logging.info(f"Data saved to {file_path}")


def main(
    organization_url: str,
    project: str,
    pat: str,
    prefixes: list[str],
    output_file: str,
) -> None:
    """
    Main function to orchestrate the process.
    """
    logging.info("Starting the process...")

    try:
        connection = setup_connection(organization_url, pat)
        logging.info("Connected to Azure DevOps.")

        repositories = get_matching_repositories(connection, project, prefixes)
        logging.info(
            f"Found {len(repositories)} repositories matching the prefixes."
        )

        all_builds = []
        all_pipelines = []

        for repo in repositories:
            builds, pipelines = process_repository(connection, project, repo)
            all_builds.append(builds)
            all_pipelines.append(pipelines)

        flat_data = flatten_data(repositories, all_builds, all_pipelines)
        save_to_csv(flat_data, output_file)
        logging.info("Process completed successfully.")

    except Exception as e:
        logging.exception(f"An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    ORGANIZATION_URL = "https://dev.azure.com/your-organization"
    PROJECT = "YourProject"
    PAT = "your-personal-access-token"
    REPOSITORY_PREFIXES = ["prefix1", "prefix2"]
    OUTPUT_FILE = "azure_devops_data.csv"

    main(ORGANIZATION_URL, PROJECT, PAT, REPOSITORY_PREFIXES, OUTPUT_FILE)
