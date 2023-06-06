phone = input("Enter password: ")
no_password = len(phone)

if  no_password < 6:
 print ("password is too short")

if (no_password >= 6) & (no_password <= 20):
 print("*" * no_password)

if no_password > 20:
 print ("password is too long")
