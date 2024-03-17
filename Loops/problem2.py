numbers= [2,4,5,6,7,8,9]

count = 0
for num in numbers:

    if(num % 2== 0):

        count = num + count
        print(num, end="\n")

print(f"Sum of the number's is: {count}")