# ruff: noqa: TRY401
import csv
import logging as logger
import sys
from typing import Any

from azure.devops.connection import Connection
from azure.devops.v7_0.build.models import Build
from azure.devops.v7_0.git.models import GitRepository
from azure.devops.v7_0.release.models import ReleaseDefinition
from msrest.authentication import BasicAuthentication

logger.basicConfig(
    level=logger.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logger.StreamHandler(sys.stdout)],
)


class AzureProcessor:
    def __init__(self, pat: str, organization_url: str, project: str):
        self.pat = pat
        self.organization_url = organization_url
        self.project = project

        self.connection = self.setup_connection()
        self.git_client = self.connection.clients.get_git_client()
        self.build_client = self.connection.clients.get_build_client()
        self.release_client = self.connection.clients.get_release_client()
        logger.info("Connected to Azure DevOps.")

    def setup_connection(self) -> Connection:
        credentials = BasicAuthentication("", self.pat)
        return Connection(base_url=self.organization_url, creds=credentials)

    def get_matching_repositories(
        self, prefixes: list[str]
    ) -> list[GitRepository]:
        repositories = self.git_client.get_repositories(self.project)
        matching = []
        for repo in repositories:
            if any(repo.name.startswith(prefix) for prefix in prefixes):
                matching.append(repo)
        return matching

    def get_repository_builds(self, repository_id: str) -> list[Build]:
        return self.build_client.get_builds(
            self.project, repository_id=repository_id
        )

    def get_repository_pipelines(
        self, repository_id: str
    ) -> list[ReleaseDefinition]:
        return self.release_client.get_release_definitions(
            self.project, artifact_source_id=repository_id
        )

    def process_repository(
        self, repo: Any
    ) -> tuple[list[Build], list[ReleaseDefinition]]:
        repo_id = repo.id
        repo_name = repo.name
        logger.info(f"Processing repository: {repo_name}")

        builds = []
        try:
            builds = self.get_repository_builds(repo_id)
            logger.info(
                f"Found {len(builds)} builds for repository {repo_name}."
            )
        except Exception as e:
            logger.exception(
                f"Error retrieving builds for repository {repo_name}: {str(e)}"
            )

        pipelines = []
        try:
            pipelines = self.get_repository_pipelines(repo_id)
            logger.info(
                f"Found {len(pipelines)} pipelines for repository {repo_name}."
            )
        except Exception as e:
            logger.exception(
                f"Error retrieving pipelines for repository {repo_name}: {str(e)}"
            )

        return builds, pipelines


def create_base_record(repo: Any) -> dict[str, Any]:
    return {
        "repository_id": repo.id,
        "repository_name": repo.name,
        "repository_url": repo.url,
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
    repo: Any, builds: list[Build]
) -> list[dict[str, Any]]:
    flattened_data = []

    for build in builds:
        record = create_base_record(repo)
        record.update(
            {
                "build_id": build.id,
                "build_number": build.build_number,
                "build_status": build.status,
                "build_result": build.result,
                "build_url": build.url,
            }
        )
        flattened_data.append(record)

    return flattened_data


def flatten_repository_with_pipelines(
    repo: Any, pipelines: list[ReleaseDefinition]
) -> list[dict[str, Any]]:
    flattened_data = []

    for pipeline in pipelines:
        record = create_base_record(repo)
        record.update(
            {
                "pipeline_id": pipeline.id,
                "pipeline_name": pipeline.name,
                "pipeline_url": pipeline.url,
            }
        )
        flattened_data.append(record)

    return flattened_data


def flatten_data(
    repositories: list[Any],
    builds_data: list[list[Build]],
    pipelines_data: list[list[ReleaseDefinition]],
) -> list[dict[str, Any]]:
    flat_data = []

    for i, repo in enumerate(repositories):
        builds = builds_data[i]
        pipelines = pipelines_data[i]

        if not builds and not pipelines:
            flat_data.append(create_base_record(repo))

        flat_data.extend(flatten_repository_with_builds(repo, builds))

        flat_data.extend(flatten_repository_with_pipelines(repo, pipelines))

    return flat_data


def save_to_csv(data: list[dict[str, Any]], file_path: str) -> None:
    if not data:
        logger.warning("No data to save.")
        return

    field_names = data[0].keys()

    with open(file_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

    logger.info(f"Data saved to {file_path}")


def main(
    organization_url: str,
    project: str,
    pat: str,
    prefixes: list[str],
    output_file: str,
) -> None:
    logger.info("Starting the process...")

    try:
        azp = AzureProcessor(pat, organization_url, project)
        repositories = azp.get_matching_repositories(prefixes)
        logger.info(
            f"Found {len(repositories)} repositories matching the prefixes."
        )

        all_builds = []
        all_pipelines = []

        for repo in repositories:
            builds, pipelines = azp.process_repository(repo)
            all_builds.append(builds)
            all_pipelines.append(pipelines)

        flat_data = flatten_data(repositories, all_builds, all_pipelines)
        save_to_csv(flat_data, output_file)
        logger.info("Process completed successfully.")

    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    ORGANIZATION_URL = "https://dev.azure.com/your-organization"
    PROJECT = "YourProject"
    PAT = "your-personal-access-token"
    REPOSITORY_PREFIXES = ["prefix1", "prefix2"]
    OUTPUT_FILE = "azure_devops_data.csv"

    main(ORGANIZATION_URL, PROJECT, PAT, REPOSITORY_PREFIXES, OUTPUT_FILE)
