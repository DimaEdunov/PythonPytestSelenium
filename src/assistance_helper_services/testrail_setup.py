import pytest


@pytest.fixture
def get_request_object(request):
    return request


def test_get_all_test_names(get_request_object):
    request_object = get_request_object
    test_names = []
    for item in request_object.session.items:
        if isinstance(item, pytest.Function):
            test_names.append(item.name)

    # Print the list of test names
    print(test_names)