users_forgotten_password = "emily"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != users_forgotten_password and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter password: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You are out of guesses!")
else:
    users_forgotten_password = True
    print("Password correct")

# case sensitive strings