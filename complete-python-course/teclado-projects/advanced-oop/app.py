from admin import Admin
from database import Database
from user import User

a = Admin('rolf', '1234', 3)
u = User('Bob', 'boy97')

users = [a, u]

for user in users:
    user.save()

print(Database.find(lambda x: x['username'] == 'rolf'))
