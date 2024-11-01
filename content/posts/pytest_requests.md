Title: Requests using pytest
Date: 2023-09-02  
Tags: pytest, requests, python  
Summary: Small setup for testing HTTP requests using pytest

# Pytest and requests

This module provides a pytest fixture to mock HTTP requests.
It provide custom responses based on response files.

## Response files

Response files are organized in the 'tests/responses' directory.

Each response file is placed within a subdirectory named after the URI of the URL being tested.
This ensures responses are matched accurately with test URLs.

### File naming

Response files should be named based on the following convention:

```.text
HTTP_METHOD_query_parameters.txt
```

- HTTP_METHOD represents the HTTP method to be mocked (e.g., GET, POST).
- query*parameters represent query parameters, separated by underscores (*) if there are multiple.

## Running Tests

When a test function is executed, it uses the `http_request_fixture` to intercept HTTP requests and
It return custom responses based on the corresponding response file.

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

**Mock file path**

```.shell
|- tests
   |- responses
      |- path_to_resource
         |- param1_value1_param2_value2.txt
```

**Mock file content**

```{ .text }
--8<-- "code/pytest_requests/mock_file.txt"
```

## Code

```{ .python }
--8<-- "code/pytest_requests/tests.py"
```

## Extracting Responses from actual API

```{ .python }
--8<-- "code/pytest_requests/extract.py"
```
