user = {
    "username": "Jose1234",
    "access_level": "guest"
}


def user_has_permission(func):
    # if user.get("access_level") == "admin":
    #     return func
    # raise RuntimeError
    def secure_func():
        if user.get("access_level") == "admin":
            return func()

    return secure_func


def my_function():
    return "Password for admin panel is 1234."


my_secure_function = user_has_permission(my_function)
print(my_secure_function())
