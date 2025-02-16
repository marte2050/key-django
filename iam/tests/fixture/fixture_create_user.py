import pytest
from users.models import User


@pytest.fixture(autouse=True)
def create_user_without_admin_permission(db) -> None:
    User.objects.create_user("test_user_common", "test@test.com", "test")


@pytest.fixture(autouse=True)
def create_user_with_admin_permission(db) -> None:
    User.objects.create_superuser("test_user_admin", "test@test.com", "test")
