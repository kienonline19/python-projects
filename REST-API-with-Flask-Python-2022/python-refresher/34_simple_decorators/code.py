user = {
    "username": "Jose",
    "access_level": "guest"
}


def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


# def secure_get_admin():
#     if user["access_level"] == "admin":
#         return "1234"


# if user["access_level"] == "admin":
#     print(get_admin_password())

# print(secure_get_admin())

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
