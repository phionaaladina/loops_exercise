#1. Print First 10 natural numbers using while loop.
nat_num = 1

while nat_num <= 10:
    print(nat_num)
    nat_num += 1



#2. Calculate the sum of all numbers from 1 to a given number.

# initialize sum and counter
_num = int(input('Please enter a number'))
sum = 0
count = 1

while count <= _num:
      sum = sum + count
      count = count + 1
print("The sum is", sum)



'''3. Write a program to print multiplication table of a given number. 
  eg if number is 2, then output should be 2, 4, 6, 8 ..'''

num = int(input('Please enter a number: '))
count = 1

print ("The Multiplication Table of: ", num)    
for count in range(1, 13):      
 print (num, 'x', count, '=', num * count) 

 '''4. Write a program to display only those numbers from a list that satisfy 
the following conditions
The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
given `numbers = [12, 75, 150, 180, 145, 525, 50]`'''



numbers_list = [12, 75, 150, 180, 145, 525, 50]

for num in numbers_list:
 if num % 5 == 0: 
  if(num > 150):
    continue 
  print(num)
      
         


'''5. Write a program to count the total number of digits in a number
using a while loop. given number `4673453`'''


number = 4673453
count=0
while(number>0):
    count=count+1
number=number//10
print("The number of digits in the number are:",count)



# #6. Display numbers from -10 to -1 using while loop

num_start = -10
num_end = -1

while num_start <= num_end:
     if num_start < 0:
        print(num_start, end = '   ')
     num_start = num_start + 1

