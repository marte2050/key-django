import pytest
from django.test import Client


@pytest.fixture
def client_admin_logged_in() -> Client:
    client = Client()
    client.login(username="test_user_admin", password="test")  # noqa: S106
    return client


@pytest.fixture
def client_noadmin_logged_in() -> Client:
    client = Client()
    client.login(username="test_user_common", password="test")  # noqa: S106
    return client
