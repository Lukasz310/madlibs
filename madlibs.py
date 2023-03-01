# string concatenation (aka how to put strings toghether)
# supose we wont to create a string that says "subscribe to ______"
# youtuber = ""

# # a few ways to do this
# print ("subscribe to " + youtuber)
# print ("subscribe to {}".format(youtuber))
# print (f"subscribe to {youtuber}")

adj = input("Adjetive: ")
verb1 = input("VERB1: ")
verb2 = input("VERB2: ")
fameous_person = input("Fameous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so exited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {fameous_person}!"

print(madlib)