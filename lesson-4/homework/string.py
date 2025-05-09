2.Write a Python script to add a key to a dictionary.
name={0: 10, 1: 20}
name ['2'] =30
print(name)

3.Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
nam={** dic1, **dic2, **dic3} 
print(nam)

4. Generate a Dictionary with Squares
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary (n = 5):
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n=5
AAA={x:x*x for x in range(1,n+1)}
print(AAA)

5. Dictionary of Squares (1 to 15)
Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
Expected Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
n=15
AAA={x:x*x for x in range(1,n+1)}
print(AAA)

Set Exercises
1. Create a Set
Write a Python program to create a set.
my_set={1,2,3,'q','w'}
for AAA in my_set:
  print(AAA)

2. Iterate Over a Set
Write a Python program to iterate over sets.
my_set={1,2,3,'q','w'}
print("Iterating over the set:")
for item in my_set:
  print(item)

3. Add Member(s) to a Set
Write a Python program to add member(s) to a set.
my_set={1,2,3,'q','w'}
my_set.add(123)
print(my_set)

4. Remove Item(s) from a Set
Write a Python program to remove item(s) from a given set.
my_set={1,2,3,'q','w'}
my_set.remove('w')
print(my_set)

5. Remove an Item if Present in the Set
Write a Python program to remove an item from a set if it is present in the set.
my_set={1,2,3,'q','w'}

rem=1
if rem in my_set:
    my_set.remove(rem)
    print(f'item {rem} ochdi')
else:
    print(f'item{rem}not found')
print(my_set)

















