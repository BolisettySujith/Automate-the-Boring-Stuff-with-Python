# LISTS

## Practice Questions

1. What is []?

    > It is an empty list, which contain no items.

    > A list begins with an opening square bracket and ends with a closing square bracket, [ ].
    
    >The '[ ]' is used for placaing values in lists.


2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].) 

    > spam[2] = 'hello'

 For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd']. 

3. What does spam[int(int('3' * 2) // 11)] evaluate to?

    > spam[int(int('3' * 2) // 11)] 
    
    > 'd'

4. What does spam[-1] evaluate to?

    > spam[-1] 
    
    > 'd'

5. What does spam[:2] evaluate to?
    
    > spam[:2]

    > [ 'a' , 'b' ]

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

6. What does bacon.index('cat') evaluate to?

    >  bacon.index('cat')

    > 1

7. What does bacon.append(99) make the list value in bacon look like?

    > bacon.append(99)  

    > It will append value 99 in the bacon list.

    > [3.14, 'cat', 11, 'cat', True, 99]

8. What does bacon.remove('cat') make the list value in bacon look like?

    >  bacon.remove('cat') 

    > It will remove first occuring 'cat' value from the bacon list.

    > [3.14, 11, 'cat', True, 99]

9. What are the operators for list concatenation and list replication?

    >  list concatenation = ' + '.

    > list replication = ' * '.

10. What is the difference between the append() and insert() list methods?

    > ' append() ' => It will place the value entreing in last index of a list.

    > ' insert() ' => It will place value at any index based on what index the user inputs.

11. What are two ways to remove values from a list?

    > 'list name'.remove( )

    > del 'list name'[ ] => it will delete the input index typed by the user. 

12. Name a few ways that list values are similar to string values.

    > The len( ) function will return the number of values that are present  in a 'list'.

    > The len( ) function will also return the number of characters that are present in a 'String'.

13. What is the difference between lists and tuples?

    > Lists are 'mutable'.

    > The user can add, remove and they can be modified the values in the lists.
    
    >tuples are immutable.

    >Tuples cannot have their values modified.

14. How do you type the tuple value that has just the integer value 42 in it?

    > tup = (42)

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
    > **tuple(list name)**

    > **list(tuple name)**

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

    >The variables don't contain list valuesbut they contain **reference** to the list

17. What is the difference between copy.copy() and copy.deepcopy()?

    > **copy.copy()** => Used to copy of a mutable value like list or dictionary not just a small reference. 

    > **copy.deepcopy()** => Used to copy the lists inside the lists


