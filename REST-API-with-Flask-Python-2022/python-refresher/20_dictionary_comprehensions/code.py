users = [ 
    (0, "Bob", "bob123"),
    (1, "John", "tiny&"),
    (2, "Jen", "jen*34"),
    (3, "David", "hello@123"),
    (4, "Jonas", "boy9756")
]

username_mapping = {
    user[1]: user 
    for user in users
}

# print(username_mapping["Jonas"])

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

if username_input in username_mapping:
    _, username, password = username_mapping[username_input]
    
    if password_input == password:
        print("Your details are correct!")
    else:
        print("Your details are incorrect.")
else:
    print("Your details are incorrect.")
