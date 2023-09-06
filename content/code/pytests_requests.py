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
