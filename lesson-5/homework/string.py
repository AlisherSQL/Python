2. Conditional Statements Exercise
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Input Format
A single line containing a positive integer, n.
Constraints
1 <= n <= 100

def chek_weird (n):
     if n%2!=0:
       print ('Weird')
     elif 2<= n <=5:
         print ('Not Weird')
     elif 6<= n <=20:
            print ('Weird')
     elif 20 < n:
          print ('Not Weird')
print(chek_weird(3))

3.Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
Give two solutions.

Solution 1 with if-else statement.

Solution 2 without if-else statement.

a=int(input())
b=int(input())

for number in range (a,b):
    if number % 2==0:
        print (number)







                                           
