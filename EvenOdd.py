numbers= (1,2,3,4,5,6,7,8,9) 

even_count=0
odd_count=0

for x in numbers:

    if not x % 2:
       even_count += 1

    else: 
      odd_count += 1

print ("Even numbers in the list:", even_count)
print ("odd numbers in the list :", odd_count)