name=input("what is your name?")
print("nice to meet you,",name)
age=input("what is your age?")
try:
    age=int(age)
    print("you were born in", 2025-age)
except ValueError:
    print("that is not a proper age/number")
    print("dont be smart with me")
except NameError:
    print("you are misspelling something")
except:
    print("this will cath all other exception")
else:#only is no exception is runned
    print("thanks for playing fair")
finally:#this happens always
    print("this will be done no matter what")