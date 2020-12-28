# DICTIONARIES AND STRUCTURING DATA

## Practice Questions

1. What does the code for an empty dictionary look like?

    > Dic = { }

2. What does a dictionary value with a key 'foo' and a value 42 look like?

    > X = { 'foo' : 42 } 
3. What is the main difference between a dictionary and a list?

    >Lists - Having only one function of string.

    >Dictionaries - Having two functions of string(**key, value**)

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

    >the user will get an error.

    >keyerror : 'foo'

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

    >spam ={'cat':'cat'}

    >'cat' in spam means, spam['cat'] it will give the value of cat, is cat.
 
    
    >'cat' in spam.keys(),  the cat is a key word.



6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

    >spam ={'cat':'Tiger'}
    
    >'cat' in spam means, spam['cat'] it will give the value of cat, cat.
 
    >'cat'in spam.values(),
    cat is the value of spam.values() 

    
7. What is a shortcut for the following code?

    -----------------------

    if 'color' not in spam:
    spam['color'] = 'black'

    ----------------------

    >spam.setdefault('colour':'Black')

8. What module and function can be used to “pretty print” dictionary values?

    >module is **pprint**

    > function is **pprint.pprint()**

