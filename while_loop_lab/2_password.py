username = input()
password = input()

while True:
    input_password = input()

    if password == input_password:
        print(f'Welcome {username}!')
        break

# input_password = input()
# while input_password != password:
#     input_password = input()
# print(f'Welcome {username}!')