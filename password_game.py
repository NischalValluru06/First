correct_password = "supercalifragilisticexpialidocious"
attempt = str(input("Please type in the password: "))
if attempt == "supercalifragilisticexpialidocious":
    print("That is the correct password. You have been granted access. ")
else:
    print("Incorrect. You have been locked out. ")
