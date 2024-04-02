#Even number generator using yield keyword.abs

def evenNumber(num):

    for i in range(2, num+1, 2):

        yield i

for i in evenNumber(10):

    print(i);

#! For more detail about this concept you can go through the "about.md" in this repo.