import random
import math

def generate_random():
    count=int(input("Please enter how many random numbers you want to generate:"))
    numbers_list=[]
    aux=count
    while aux>0:
        aux -=1
        a=random.randint(1,100)
        numbers_list.append(a)
    return numbers_list

def permutation_sort(a,step):
    num=len(a)
    step1=0;
    numberofsteps=0
    while (is_sorted(a)==False):
        if(step1<step):
            step1 +=1
            numberofsteps += 1
            shuffle(a)

        else:
            print("step " + str(numberofsteps))
            numberofsteps += 1
            step1 = 1
            print(a)
            shuffle(a)

    print("Your set of numbers is now sorted after step "+ str(numberofsteps))
    print(a)

def is_sorted(a):
    num=len(a)
    for i in range (0,num-1):
        if a[i]> a[i+1]:
            return False
    return True

def shuffle(a):
    num = len(a)
    for i in range (0,num):
        r = random.randint(0,num-1)
        a[i], a[r] = a[r], a[i]

def comb_sort(a,step):
    shrink_fact = 1.3
    gaps = len(a)
    swapped = True
    i = 0
    step1=0
    numberofsteps = 0

    while gaps>1 or swapped:
        gaps=int(float(gaps)/shrink_fact)
        swapped= False
        i=0

        while(gaps + i <len(a)):
            if(a[i]> a[i+gaps]):
                a[i], a[i + gaps] = a[i + gaps], a[i]
                swapped= True
                step1 +=1
                numberofsteps +=1
                if(step1 ==step):
                    print("step " + str(numberofsteps))
                    print(a)
                    step1=0
            i +=1
    print("Your set of numbers is now sorted after step " + str(numberofsteps))
    print(a)


def start():
    print("Welcome to my attempt of Assignment 2")
    numbers=[]

    while True:
        print("1. Generate random natural numbers")
        print("2. Sort the numbers using permutation sort")
        print("3. Sort the numbers using comb sort")
        print("0. Exit the program")

        option=input("Please insert the command of choice:")
        if option=='1':
            numbers=generate_random()
            print(numbers)
        elif option=='2':
            step=int(input("Please enter a step number>>"))
            permutation_sort(numbers,step)
        elif option=='3':
            step = int(input("Please enter a step number>>"))
            comb_sort(numbers,step)
        elif option=='0':
            return
        else:
            print("You have inserted another option from those available")

start()