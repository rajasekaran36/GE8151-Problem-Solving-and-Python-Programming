print("Enter the number to find the root");
number=int(input())
guess = 1
while True:
    fx = guess*guess - number
    dx = 2*guess
    actual = guess - ((fx)/dx)
    actual = round(actual,4)
    if guess == actual:
        print("Root of given number ",number," is ",actual)
        break
    else:
        guess = actual