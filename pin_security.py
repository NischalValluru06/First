attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1
    if code == "1234":
        success = True
        break

    if attempts == 3:
        success = False
        break
    print("Incorrect! Please try again! ")
if success:
    print("Correct PIN entered!")
else:
    print("Max attempts reached. You have been denied access. ")
