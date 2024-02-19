## Dictionary
#### Basic of dictionary is key, value pair.


1) A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.

2) Basic syntex of dictionary is:
```python
    dict1= {'key': 'value'} 
    #firt element always be an key and second one will always be an value.
    print(dict1)

```

3) We can reterive our elements by using our indexing method as we did in `list`.

```python
    print(dict1['Sonam'])   #90
```
And other way is by using predefined `get()` for dictionary.

```python
    print(dict1.get('Sonam'))   #90
```

* Here the main difference between reteriving the elements by `indexing` and `get()` is:
<br>`Indexing` not handles the error while,    `get()` handles the error when we use wrong key in that case.  

4) So, dictionary is `mutable` it means we can chnage the value of dictionary.

```python
    dict1['Aman']= 80   #chnage the value of Aman into 80

    print(dict1['Aman'])
```

5) We can use iteration for our dictionary elements:
```python
    for i in dict1:

        print(i, dict1[i])
```
### Or

```python
    #Imp syntex for dictionary related problems
    for key, values in dict1.items():
        
        print(key, values)
```
Here in above syntex we iterate our items of dict1 with key and value pair.