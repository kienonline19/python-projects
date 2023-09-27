import functools

user = {
    "username": "Jose1234",
    "access_level": "admin"
}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(panel):
        if user.get("access_level") == "admin":
            return func(panel)
        else:
            raise PermissionError("You aren't a admin")

    return secure_func


@user_has_permission
def my_function(panel):
    """
    Allow us to retrieve the password for the admin panel
    """
    return f"Password for {panel} panel is 1234."


@user_has_permission
def another():
    return "Hello"


print(my_function("movies"))
print(another())
