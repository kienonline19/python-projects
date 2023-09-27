def add_all(*args):
    return sum(args)


def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f"For {k} we have {v}.")


nums = (1, 3, 5, 7)
print(add_all(*nums))

pretty_print(username='jose123', access_level='admin')
print('-' * 30)
pretty_print(**{'username': 'jose123', 'access_level': 'admin'})
