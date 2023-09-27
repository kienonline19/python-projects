import functools

"""
guest: 0
user: 1
admin: 2
"""
access_levels = {
    0: "guest",
    1: "user",
    2: "admin"
}

user = {
    "username": "Jose",
    "access_level": 2
}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] >= access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_levels[access_level]} permissions for {user['username']}"

        return secure_function
    return decorator


@make_secure(2)
def get_admin_password():
    return "admin: 1234"


@make_secure(0)
def get_dashboard_password():
    return "user: user_password"


print(get_admin_password())
print(get_dashboard_password())
