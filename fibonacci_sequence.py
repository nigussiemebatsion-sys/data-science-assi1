""" 
Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers before it.
let f(n) be the number we want to find :its mathmatical defination is :
   f(n)=f(n-1)+f(n-2) where f(0)=0 and f(1)=1  this equation works starting from n=2 and above since f(0) and f(1) are given
now we can write a code to generate fibonacci sequence based on the the mathmatical defination of the sequence. 
"""
def fibonacci(n):
    if n==0:
       return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter number of terms n: "))
if n<0:
    print("Enter a positive integer.")
elif n==0:
    print(0)
else:
    for i in range(n):
        print(fibonacci(i), end=' ')





