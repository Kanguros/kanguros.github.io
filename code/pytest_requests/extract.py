import os
from urllib.parse import urlparse, parse_qs

from requests import Response


class ApiWrapper:
    def __init__(self):
        # Initialize your API client here
        pass

    def get_data(self) -> Response:
        pass


def execute_and_save_responses(api: ApiWrapper):
    responses = {}

    # Define the methods to execute with arguments
    methods_to_execute = {
        api.get_data: None,  # No arguments
        # Add more methods with their respective arguments as needed
    }

    for method, args in methods_to_execute.items():
        if args:
            response = method(args)  # Call the method with arguments
        else:
            response = method()  # Call the method without arguments

        # Convert the response data to a string for saving
        file_content = prepare_file_content(response)
        # Get the URL associated with the method (for response file path)
        request_url = response.request.url

        response_file_path = get_response_file(request_url)
        save_response(response_file_path, file_content)

        responses[method.__name__] = response_file_path

    return responses


def get_response_file(url: str) -> str:
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip("/").split('/')
    method = parsed_url.scheme
    query_params = parse_qs(parsed_url.query)

    query_str = "_".join([f"{param}_{value}" for param, values in query_params.items() for value in values])
    return os.path.join("tests", "responses", "_".join(path_parts), f"{method}_{query_str}.txt")


def prepare_file_content(response: Response):
    content = f"""# status_code: {response.status_code}
    # reason: {response.reson}
    {response.content}
    
    """
    return content


def save_response(file_path: str, content: str):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        file.write(content)


if __name__ == "__main__":
    api = ApiWrapper()
    responses = execute_and_save_responses(api)
    print(f"Responses saved successfully! {responses}")
