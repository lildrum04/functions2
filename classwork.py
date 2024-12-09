import random

enemy_insults = ["You fight like a dairy Farmer!",
                 "This is the END for you, you gutter crawling cur!",
                 "I've spoken with apes more polite than you!",
                 "Soon you'll be wearing my sword like a shish kebab!"]
right_comebacks = {"You fight like a dairy Farmer!": "How appropriate. You fight like a cow!",
                   "This is the END for you, you gutter crawling cur!": "And I've got a little TIP for you, get the POINT?",
                "I've spoken with apes more polite than you!": "I'm glad to hear you attended your family reunion!",
                   "Soon you'll be wearing my sword like a shish kebab!": "First you'd better stop waving it like a feather duster."}
random_comebacks = ["How appropriate. You fight like a cow!",
                    "And I've got a little TIP for you, get the POINT?",
                    "I'm glad to hear you attended your family reunion!",
                    "First you'd better stop waving it like a feather duster."]


print(random.choice(enemy_insults ))

# def randomcomeback():

for i in random_comebacks:
    print(i)
user_input = input("Enter your choice: ")






# print()
# input("pick one of the comebacks: "
#       "a." : + random.choice(random_comebacks)
#


