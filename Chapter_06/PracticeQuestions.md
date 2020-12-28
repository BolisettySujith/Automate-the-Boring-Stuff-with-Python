# MANIPULATING STRINGS

## Practice Questions

1. What are escape characters?

    >escape characters are used to use a character otherwise it is impossible to put into a string.

    > An escape character consists of a backslash ( \ ) followed by the character you want to add to the string. Eg = (\', \", \t, \n, \ \ )

2. What do the \n and \t escape characters represent?

    >**\n** represents a **new line**.

    >**\t** represents **Tab**.

3. How can you put a \ backslash character in a string?

    >For this two backslah characters are needed '\ \' 

    Eg : print('I am sujith\\')

4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?

    >While passing a string containing a single quote in side a  double quote character("") the single quote character will be printed.

5. If you don’t want to put \n in your string, how can you write a string with newlines in it?

    >A multiline string in Python without using \n in string by, using begins and ends with either three single quotes or three double quotes.

6. What do the following expressions evaluate to?
    - 'Hello, world!'[1]
    - 'Hello, world!'[0:5]
    - 'Hello, world!'[:5]
    - 'Hello, world!'[3:]

    > 'Hello, world!'[1] evaluate to **'e'**

    > 'Hello, world!'[0:5] evaluate to **'Hello'**

    > 'Hello, world!'[:5] evaluate to **'Hello'**

    >'Hello, world!'[3:] evaluate to **'lo, world!'**

7. What do the following expressions evaluate to?

    - 'Hello'.upper()
    - 'Hello'.upper().isupper()
    - 'Hello'.upper().lower()

    > 'Hello'.upper() evaluates to **'Hello'**

    >'Hello'.upper().isupper() evaluates to **True**

    >'Hello'.upper().lower() evaluates to **False**

8. What do the following expressions evaluate to?

    - 'Remember, remember, the fifth of November.'.split()
     - '-'.join('There can be only one.'.split())

    > 'Remember, remember, the fifth of November.'.split() evaluates to 
    
    >['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
    ------------


   >'-'.join('There can be only one.'.split()) evaluates to

   > 'There-can-be-only-one.'

   -----

9. What string methods can you use to right-justify, left-justify, and center a string?

    > right-justify - rjust( )

    >left-justify - ljust( )

    >center - centre( )

10. How can you trim whitespace characters from the beginning or end of a string?

    >by using **strip( ), rstrip( ), lstrip( ) methods**.