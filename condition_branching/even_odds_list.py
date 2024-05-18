# Write a Python program to count the number of even and odd numbers in a list.

numbers = [32, 34, 3, 8, 1, 90, 87]
even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
even_num_count = len(even)
odd_num_count = len(odd)

print(even_num_count)
print(odd_num_count)


    
