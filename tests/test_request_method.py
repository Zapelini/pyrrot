import pytest


@pytest.mark.parametrize('method', ['HEAD', 'POST', 'PUT', 'DELETE', 'PATCH', 'TRACE', 'OPTIONS'])
@pytest.mark.parametrize('path', ['/users', '/users?foo=bar'])
def test_execute_methods_not_found_path_with_wrong_method(client, method, path, url_example_example):
    method_to_call = getattr(client(url_example_example), method.lower())
    response = method_to_call(path)
    assert 404 == response.status_code
