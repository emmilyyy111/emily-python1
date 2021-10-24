# I wake up hungry
# If Im hungry
#     I eat Breakfast
#
# I leave my house
# If its cloudy
#     I bring an unbrella
# otherwise
# I bring sunglasses
#
# Im at a restaurant
# If I want meat
#     I order a steak
# otherwise If I want pasts
#     I order spaghetti & meatballs
# otherwise
#     I order salad.


# boolean variable to return true or false if user is male or not
is_female = False
is_short = True

if is_female and is_short:
    print("you are a short female")
elif is_female and not(is_short):
    print("you are a tiny female")
elif not(is_female) and is_short:
    print("you are not male and not short")
else:
    print('you are a tall female')




