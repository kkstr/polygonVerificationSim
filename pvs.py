import random


def randint():
    global possible
    global impossible
    global size
    global i
    global randint
    i = + 0
    possible = + 0
    impossible = + 0
    print("Enter simulation sample size for Z>0")
    size = int(input("> "))
    print("Enter upper bound value")
    upper = int(input("> "))
    print("Enter lower bound value")
    lower = int(input("> "))

    while i < size:
        global a
        global b
        global c
        a = random.randint(lower, upper)
        b = random.randint(lower, upper)
        c = random.randint(lower, upper)
        print(i/size*100, a, b, c)
        if solve(a, b, c):
            possible = possible + 1
            i += 1
        else:
             impossible = impossible + 1
             i += 1
    while i == size:
        print()
        print()
        str(print("The program returned Possible:", possible, "times"))
        str(print("The program returned Impossible:", impossible, "times"))
        print()
        print()
        print("% of Possible:", float(possible/size*100))
        print("% of Impossible:", float(impossible/size*100))
        print()
        print("Restart? (y/n)")
        terminate = input("> ")
        print()







def solve(a, b, c):
    if a + b >= c and b + c >= a and c + a >= b:
        return True
    else:
        return False


randint()

solve(a, b, c)