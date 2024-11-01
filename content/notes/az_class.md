Title: Azure Devops Class
Date: 2023-09-01
Tags: azure-devops, python  
Category: Note  
Summary: Short wrapper for Azure Devops API. Based on `azure-core`.

Here you will find a Python utility class, `AzureDevOps`, to streamline Azure DevOps interactions. The class makes it
easy to fetch closed User Stories and manage active Pull Requests.

## Features

- **User Stories Retrieval:** Fetch closed User Stories based on days, tags, and area path.

- **Pull Requests Management:** Retrieve active Pull Requests by repository prefix and authors.

## Usage

1. **User Stories:**

   ```python
   user_stories = azure_devops.get_closed_user_stories(days, tag, area_path)
   ```

2. **Pull Requests:**

    - Active Pull Requests by Repository Prefix:

      ```python
      active_pulls_by_repo = azure_devops.get_active_pull_requests_by_repo_prefix(prefix)
      ```

    - Active Pull Requests by Authors:

      ```python
      active_pulls_by_authors = azure_devops.get_active_pull_requests_by_authors(authors)
      ```

## Getting Started

1. Install packages:

   ```bash
   pip install azure-devops azure-devops-work-item-tracking azure-devops-git
   ```

2. Replace `"YOUR_ORGANIZATION_URL"` and `"YOUR_PERSONAL_ACCESS_TOKEN"`.

3. Customize example usage in the `if __name__ == "__main__":` block.

4. Run the script.

## Code

```python
from typing import List, Dict, Any
from azure.core.credentials import AzureDevOpsPATCredential
from azure.devops.connection import Connection
from azure.devops.v6_0.work_item_tracking.models import Wiql, WorkItemExpand
from azure.devops.v6_0.git.models import GitPullRequestSearchCriteria
import datetime

AZURE_ORGANIZATION_URL = "YOUR_ORGANIZATION_URL"
AZURE_PERSONAL_ACCESS_TOKEN = "YOUR_PERSONAL_ACCESS_TOKEN"


class AzureDevOps:
    def __init__(self):
        self.connection = self._create_azure_devops_connection()
        self.wit_client = self.connection.clients.get_work_item_tracking_client()
        self.git_client = self.connection.clients.get_git_client()

    def _create_azure_devops_connection(self) -> Connection:
        """Create an Azure DevOps connection instance.
        
        Returns:
            Connection: An instance of the Azure DevOps connection.
        """
        credentials = AzureDevOpsPATCredential(AZURE_PERSONAL_ACCESS_TOKEN)
        connection = Connection(base_url=AZURE_ORGANIZATION_URL, creds=credentials)
        return connection

    def get_closed_user_stories(self, days: int, tag: str, area_path: str) -> List[Dict[str, Any]]:
        """Get closed User Stories filtered by days, tag, and area path.
        
        Args:
            days (int): Number of days to consider for closed User Stories.
            tag (str): Tag to filter User Stories.
            area_path (str): Area path to filter User Stories.
            
        Returns:
            list: List of closed User Stories matching the criteria. Each User Story is represented as a dictionary with detailed fields.
                Each dictionary includes the following keys:
                - 'id' (int): Work item ID.
                - 'fields' (dict): Dictionary containing various fields of the User Story.
                    The 'fields' dictionary includes keys like:
                    - 'System.Title': Title of the User Story.
                    - 'System.AreaPath': Area path of the User Story.
                    - 'System.State': State of the User Story.
                    - 'System.Tags': Tags associated with the User Story.
                    - 'System.ChangedDate': Date when the User Story was last changed.
                    - ... and more fields based on Azure DevOps schema.
        """
        wiql_query = f"SELECT * FROM workitems WHERE [System.Tags] CONTAINS '{tag}' AND [System.State] = 'Closed' AND [System.ChangedDate] >= @today - {days} AND [System.AreaPath] = '{area_path}'"
        wiql = Wiql(query=wiql_query)
        results = self.wit_client.query_by_wiql(wiql, organization=AZURE_ORGANIZATION_URL)

        work_item_ids = [work_item.id for work_item in results.work_items]

        expand_options = WorkItemExpand.All
        user_stories = self.wit_client.get_work_items(ids=work_item_ids, expand=expand_options)

        return [us.as_dict() for us in user_stories]

    def get_git_repositories(self) -> List[Dict[str, Any]]:
        """Get a list of Git repositories.
        
        Returns:
            list: List of Git repositories. Each repository is represented as a dictionary with information including 'id', 'name', and 'url'.
        """
        repositories = self.git_client.get_repositories(organization=AZURE_ORGANIZATION_URL)
        return [repo.as_dict() for repo in repositories]

    def get_active_pull_requests_by_repo_prefix(self, prefix: str) -> List[Dict[str, Any]]:
        """Get active Pull Requests from Repositories with a given prefix.
        
        Args:
            prefix (str): Prefix of the repository name.
            
        Returns:
            list: List of active Pull Requests matching the criteria. Each Pull Request is represented as a dictionary with detailed fields.
                Each dictionary includes the following keys:
                - 'pullRequestId' (int): Pull Request ID.
                - 'title' (str): Title of the Pull Request.
                - 'repository' (dict): Dictionary containing repository information, including 'name' and 'url'.
                - ... and more fields based on Azure DevOps schema.
        """
        repositories = self.get_git_repositories()

        active_pull_requests = []
        for repo in repositories:
            if repo['name'].startswith(prefix):
                prs = self.git_client.get_pull_requests(repository_id=repo['id'],
                                                        search_criteria=GitPullRequestSearchCriteria(status="active"))
                active_pull_requests.extend(prs)

        return [pr.as_dict() for pr in active_pull_requests]

    def get_active_pull_requests_by_authors(self, persons: List[str]) -> List[Dict[str, Any]]:
        """Get active Pull Requests from Repositories created by specific persons.
        
        Args:
            persons (list): List of persons' names who created the Pull Requests.
            
        Returns:
            list: List of active Pull Requests matching the criteria. Each Pull Request is represented as a dictionary with detailed fields.
                Each dictionary includes the following keys:
                - 'pullRequestId' (int): Pull Request ID.
                - 'title' (str): Title of the Pull Request.
                - 'createdBy' (dict): Dictionary containing information about the person who created the Pull Request.
                - 'repository' (dict): Dictionary containing repository information, including 'name' and 'url'.
                - ... and more fields based on Azure DevOps schema.
        """
        active_pull_requests = []
        for person in persons:
            prs = self.git_client.get_pull_requests(creator_id=person,
                                                    search_criteria=GitPullRequestSearchCriteria(status="active"))
            active_pull_requests.extend(prs)

        return [pr.as_dict() for pr in active_pull_requests]


# Usage example
if __name__ == "__main__":
    azure_devops = AzureDevOps()

    # Example usage of User Stories function
    days = 7
    tag = "YOUR_TAG"
    area_path = "YOUR_AREA_PATH"
    user_stories = azure_devops.get_closed_user_stories(days, tag, area_path)

    # Example usage of Pull Requests functions
    prefix = "repo_prefix"
    active_pulls_by_repo = azure_devops.get_active_pull_requests_by_repo_prefix(prefix)

    authors = ["person1", "person2"]
    active_pulls_by_authors = azure_devops.get_active_pull_requests_by_authors(authors)


```
