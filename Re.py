import re

email = input("enter email: ")
email = email.strip()

if re.search("^.+@gmail\.com$", email):
    print("valid")
else:
    print("invalid")

