Title: Pytest cheatsheet
Date: 2023-11-04
Tags: pytest, cheatsheet
Summary: The cheatsheet provides a solid foundation for implementing tests in Python using `pytest`, including basic test structures, fixtures, parameterization, and using `monkeypatch` for temporary modifications during tests.

[TOC]

## Basic test

```python
def test_example():
    assert 1 + 1 == 2
```

Defines a simple test function. `pytest` identifies any function prefixed with `test_` as a test.

## Use fixture for setup and teardown

```python
import pytest

@pytest.fixture
def sample_resource():
    # Setup code
    resource = "some resource"
    yield resource
    # Teardown code


def test_resource(sample_resource):
    assert sample_resource == "some resource"
```

Creates a fixture `sample_resource` for use in tests, handling setup and teardown automatically.

## Parametrize tests

```python
import pytest

@pytest.mark.parametrize("input,expected", [(1, 2), (2, 3)])
def test_increment(input, expected):
    assert input + 1 == expected
```

Runs the same test function with different sets of parameters.

## Use fixtures with parameters

```python
import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param


def test_numbers(number):
    assert number < 4
```

Creates a fixture that is called multiple times with different parameters.

## Group tests in class

```python
class TestExample:
    def test_one(self):
        assert 1 + 1 == 2

    def test_two(self):
        assert 2 + 2 == 4
```

Groups related tests within a test class.

## Skip a test

```python
import pytest

@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")
def test_feature():
    ...
```

Skips the test if the condition (Python version < 3.7 in this case) is true.

## Expect an Exception

```python
import pytest

def test_exception():
    with pytest.raises(ValueError):
        raise ValueError("error")
```

Tests that a `ValueError` is raised within the context block.

## Override a value

```python
def test_change_dict(monkeypatch):
    mock_dict = {"key": "mock_value"}
    monkeypatch.setattr("module.dict_name", mock_dict)
    from module import dict_name
    assert dict_name["key"] == "mock_value"
```

Uses `monkeypatch` to override a dictionary in a module temporarily for the test.

## Override environment variable

```python
def test_env_var(monkeypatch):
    monkeypatch.setenv("ENV_VAR", "mock_value")
    assert os.environ["ENV_VAR"] == "mock_value"
```

Sets an environment variable for the duration of the test.

## Mock a function or method

```python
def mock_function():
    return "mocked!"

def test_mock_function(monkeypatch):
    monkeypatch.setattr("module.function_name", mock_function)
    from module import function_name
    assert function_name() == "mocked!"
```

Replaces a function in a module with a mock function.
