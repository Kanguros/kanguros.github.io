Title: Requests using pytest
Date: 02/09/2023  
Tags: pytest, requests, python  
Status: draft  
Summary: Small setup for testing HTTP requests using pytest

# Pytest and requests

This module provides a pytest fixture to mock HTTP requests.
It provide custom responses based on response files.

## Adding new response

1. Go to the 'tests/responses' directory.
2. Create a subdirectory for the endpoint you want to mock or locate the existing one.
3. Inside the endpoint directory, create a text file with this name format:
   `HTTP_METHOD_query_parameters.txt`

   HTTP_METHOD with the HTTP method (e.g., GET, POST).
   query_parameters with the query parameters, separated by underscores if multiple.
4. Open the file and format it like this:

```text
# status code: STATUS_CODE
# reason: REASON
BODY
```

5. Replace:
    - `STATUS_CODE` with the desired HTTP status code (e.g., 200, 404).
    - `REASON` with the reason for the status code (e.g., "OK", "Not Found").
    - `BODY` with the response content to mock.
6. Save the file.

### Example

#### test_example.py

```python
import pytest
import requests

# Import the custom fixture from conftest.py
from conftest import http_request_fixture


def test_http_request(http_request_fixture):
    # Define the URL to make an HTTP request
    url = "https://example.com/path/to/resource?param1=value1&param2=value2"

    # Perform an HTTP request
    response = requests.get(url)

    # Check the response status code
    assert response.status_code == 404  # This status code comes from the response file

    # Check the response reason
    assert response.reason == "Not Found"

    # Check the response content (assuming a specific expected response in the file)
    expected_response = "Response body content for 404 status code"
    assert response.text.strip() == expected_response

```

#### Mock file path

```
- tests
-- responses
--- path_to_resource_param1_value1_param2_value2.txt
```

#### Mock file content

```text
# status code: 404
# reason: Not Found
Response body content for 404 status code
```

## Code

```python
import os
from typing import List, Tuple
from urllib.parse import urlparse, parse_qs

import pytest
import requests
from requests import Response


def get_response_directory(url: str) -> str:
    """
    Get the directory path for response files based on the URL.
    """
    parsed_url = urlparse(url)
    uri = parsed_url.path
    return os.path.join("tests", "responses", uri)


def get_response_file(response_directory: str, method: str, query_params: dict) -> str:
    """
    Get the response file path based on the response directory, method type, and query parameters.
    """
    query_str = "_".join([f"{param}_{value}" for param, values in query_params.items() for value in values])
    return os.path.join(response_directory, method, f"{query_str}.txt")


def load_response_content(response_file: str) -> List[str]:
    """
    Load the content of a response file.
    """
    with open(response_file, "r") as file:
        return file.readlines()


def extract_response_info(content_lines: List[str]) -> Tuple[int, str, str]:
    """
    Extract response information from response content lines.
    """
    status_code = 200
    reason = ""
    body = []

    for index, line in enumerate(content_lines):
        line = line.strip()
        if not line.startswith("# "):
            body = content_lines[index:]
            break

        line_parts = line.split(":", maxsplit=1)
        line_key = line_parts[0]
        line_value = line_parts[1].strip()

        if "status_code" in line_key:
            status_code = int(line_value)
        elif "reason" in line_key:
            reason = line_value

    return status_code, reason, "\n".join(body)


def create_mock_response(status_code: int, reason: str, body: str) -> Response:
    """
    Create a mocked HTTP response.
    """
    response = Response()
    response.status_code = status_code
    response.reason = reason
    response._content = body.encode("utf-8")
    return response


@pytest.fixture
def http_request_fixture(monkeypatch):
    """
    Pytest fixture to mock HTTP requests and provide custom responses based on response files.
    """

    def mock_request(*args, **kwargs):
        url = args[1]
        method = args[0]
        query_params = parse_qs(urlparse(url).query)

        response_directory = get_response_directory(url)
        response_file = get_response_file(response_directory, method, query_params)

        content_lines = load_response_content(response_file)
        status_code, reason, body = extract_response_info(content_lines)

        return create_mock_response(status_code, reason, body)

    monkeypatch.setattr(requests.sessions.Session, "request", mock_request)


```