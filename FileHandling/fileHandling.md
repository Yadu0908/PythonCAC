### In this readme file we will see how our file handling is work on python.

1. File handling-: Besically a file handling is a way to `create`/ `read` or `write` the data inside the file.

Let's say we want to fetch the data inside the file. 
Then besically we just have to use `open('Path//fileName.extension')`.
<br>
Then we can easily open the file into our terminal through the `readline()`.
<br>
Now let, we

```python

    fileOpen= open('problem1.py')
    #and for showing the text

    fileOpne.readline()

```
<br>

But, Here is a catch.
as we all know that python has an built-in function name `__next__()`, which is generally used for iterating the values in `Loops and Comprehension`.
So, It mean we can also write the file data through `__next__()`.


```python

    fileOpen= open('problem1.py')

    fileOpen.__next__()

```
Now, The question might arise after this few discussion that how `readline()` and `__next__()` is different from each other.

So the answer is `Handling of exceptions`. Yeah!!! <br>
while using `readline()` we always have an advantage of not getting error when we are done with reading of whole line from the file.

But, 

When we use `__next__()` and we read all the file then we got an exception name `StopIteration`.
Which mean it will raise an exception after reading the whole file.