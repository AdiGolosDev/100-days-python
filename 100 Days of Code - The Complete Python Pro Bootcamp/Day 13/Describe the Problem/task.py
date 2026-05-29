def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# looping over the if statement 20 times
# 2. When is the function meant to print "You got it"?
# on the last iteration of the loop when i == 20(range(1,20) doesn't include 20)
# 3. What are your assumptions about the value of i?
# i takes the value of an integer in the range 1 - 20