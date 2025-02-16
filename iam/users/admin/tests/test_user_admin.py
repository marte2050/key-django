from users.models import User


class DataUser:
    data_to_create_user = {
        "username": "username",
        "password1": "password@123@",
        "password2": "password@123@",
        "usable_password": "true",
    }

    data_to_to_add_more_fields = {
        "username": "username",
        "first_name": "firstname",
        "last_name": "lastname",
        "email": "email@teste.com.br",
        "is_active": True,
        "is_staff": True,
    }


def test_when_the_user_is_allowed_to_create_a_new_user(client_admin_logged_in):
    url = "/admin/users/user/add/"
    username = DataUser.data_to_create_user.get("username")
    data_to_create_user = DataUser.data_to_create_user
    data_to_to_add_more_fields = DataUser.data_to_to_add_more_fields
    first_response = client_admin_logged_in.post(url, data_to_create_user)

    client_admin_logged_in.post(first_response.url, data_to_to_add_more_fields)
    user = User.objects.get(username=username)

    response_expected = {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "is_active": user.is_active,
        "is_staff": user.is_staff,
    }

    assert response_expected == DataUser.data_to_to_add_more_fields  # noqa: S101


def test_when_the_user_has_permission_they_can_change_the_password(
    client_admin_logged_in,
):
    user = User.objects.get(username="test_user_admin")
    url = f"/admin/users/user/{user.id}/password/"
    new_password = "password1112"  # noqa: S105

    client_admin_logged_in.post(
        url, {"password1": new_password, "password2": new_password}
    )

    login_ok = client_admin_logged_in.login(
        username=user.username, password=new_password
    )

    assert login_ok  # noqa: S101


def test_when_the_user_does_not_have_permission_to_create_a_user_it_should_return_an_error(  # noqa: E501
    client_noadmin_logged_in,
):
    url = "/admin/users/user/add/"
    data_to_create_user = DataUser.data_to_create_user
    data_to_to_add_more_fields = DataUser.data_to_to_add_more_fields
    first_response = client_noadmin_logged_in.post(url, data_to_create_user)

    response = client_noadmin_logged_in.post(
        first_response.url, data_to_to_add_more_fields
    )

    content = response.content.decode()
    response_expected = "Você está autenticado como test_user_common, mas não está autorizado a acessar esta página."  # noqa: E501

    assert response_expected in content  # noqa: S101
