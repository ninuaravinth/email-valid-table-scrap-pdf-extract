
import re

email = re.compile(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
email1 = re.compile(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}[.]\w{2,3}$")
  
# there may be name@gmail.com and somename@domain.co.in or somename@domain.org.in
user_input = input("Enter your mail: ")
  

if re.fullmatch(email,user_input):
    print(f"'{user_input}' is Valid")
elif re.fullmatch(email1,user_input):
    print(f"'{user_input}'is valid")
else:
    print(f"'{user_input}' is Invalid")
