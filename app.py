is_animal = True
is_cat = True
is_cute = True

if is_animal and not is_cat:
    print("You are a animal, but not a cat. Not a cat indeed")
elif is_animal and is_cat and is_cute:
    print("You are a cute cat")
else:
    print("You are not a cat neither an animal, what are you?")