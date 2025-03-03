import os
from urllib.parse import parse_qs, urlparse

import pytest
import requests
from requests import Response

BASE_RESPONSE_PATH = os.path.join("tests", "responses")


def get_response_file(url: str) -> str:
    """
    Get the response file path based on the URL.
    """
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip("/").split("/")
    method = parsed_url.scheme

    query_params = parse_qs(parsed_url.query)
    query_str = "_".join(
        [
            f"{param}_{value}"
            for param, values in query_params.items()
            for value in values
        ]
    )

    dir_name = "_".join(path_parts)
    file_name = f"{method}_{query_str}.txt"

    return os.path.join(BASE_RESPONSE_PATH, dir_name, file_name)


def load_response_content(response_file: str) -> list[str]:
    """
    Load the content of a response file.
    """
    with open(response_file) as file:
        return file.readlines()


def extract_response_info(content_lines: list[str]) -> Response:
    """
    Extract response information from response content lines and create a Response object.
    """
    status_code = 200
    reason = ""
    body = []

    for line in content_lines:
        line = line.strip()
        if not line.startswith("# "):
            body.append(line)
        else:
            line_parts = line.split(":", maxsplit=1)
            line_key = line_parts[0]
            line_value = line_parts[1].strip()

            if "status_code" in line_key:
                status_code = int(line_value)
            elif "reason" in line_key:
                reason = line_value

    response = Response()
    response.status_code = status_code
    response.reason = reason
    response._content = "\n".join(body).encode("utf-8")
    return response


@pytest.fixture
def http_request_fixture(monkeypatch):
    """
    Pytest fixture to mock HTTP requests and provide custom responses based on response files.
    """

    def mock_request(*args, **kwargs):
        url = args[1]

        response_file = get_response_file(url)
        content_lines = load_response_content(response_file)
        return extract_response_info(content_lines)

    monkeypatch.setattr(requests.sessions.Session, "request", mock_request)
