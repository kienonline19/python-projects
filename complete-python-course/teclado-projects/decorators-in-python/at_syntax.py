user = {
    "username": "Jose1234",
    "access_level": "admin"
}


def user_has_permission(func):
    def secure_func():
        """
        Hey
        """
        if user.get("access_level") == "admin":
            return func()
        else:
            raise PermissionError("You aren't a admin")

    return secure_func


# my_secure_function = user_has_permission(my_function)
@user_has_permission
def my_function():
    """
    Allow us to retrieve the password for the admin panel
    """
    return "Password for admin panel is 1234."


@user_has_permission
def another():
    ...


print(another.__name__)
print(my_function.__name__)
print(my_function.__doc__)
