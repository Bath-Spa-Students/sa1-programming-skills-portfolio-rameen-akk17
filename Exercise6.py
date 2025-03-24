correct_password = "12345"

attempt = input("enter password: ").strip()

while attempt != correct_password:
    print("Incorrect, Try again")
    attempt = input("enter password: ").strip()

print("Correct")


