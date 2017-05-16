import re
s = "aa@a.is"
pat = re.match(r"^(.@[a-zA-Z0-9]+\.(?:is|com))$", s)
if pat is None:
    print("Not a valid email")
else:
    print("Found an email!!!")

