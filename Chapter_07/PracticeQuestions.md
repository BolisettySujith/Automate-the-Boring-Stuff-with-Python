# PATTERN MATCHING WITH REGULAR EXPRESSIONS

## Practice Questions

1. What is the function that creates Regex objects?

    >re.compile(r'\d{3}-\d{3}-\d{4}')
2. Why are raw strings often used when creating Regex objects?
    
    >Raw strings make the string more easy to extract a pattren.The raw strings will match every type of charecter based on the user input instead of placing the correct string.
3. What does the search() method return?

    >When a user is looking for a pattren if the pattren found, the search() method **returns the match object**.

    > If not found, the search method **returns None**.
4. How do you get the actual strings that match the pattern from a Match object?

    >first **importing the regex module**.

    >**compiling** the pattren of raw strings.

    > **searching** the pattren in the actual string.

    >**grouping** the searched pattren.

5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

    >group 0 will cover entire pattren.

    >group 1 will cover first 3 characters in the pattren.

    >Group 2 will cover remaining 7 charecters in the  pattren.

6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

    >pranthasis and periods can be escaped with a bachslash 
    ' \ .', ' \ (', ' \ )'.
7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

    >The findall() method returns **a list of strings**.

    >Each string in the list is a piece of the searched text that matched the regular expression.
8. What does the | character signify in regular expressions?

    >The | character signify's **pipe**

    > It can be used any where to match one or more expressions.

9. What two things does the ? character signify in regular expressions?

    >There is a pattern that you want to match only optionally.

    >The ? character  flags the group that precedes it as an optional part of the pattern 

    > It will match zero instances or instance of the regular expression.

10. What is the difference between the + and * characters in regular expressions?

    >The '+' means match one or more, the group that preceeds the plus can occurs more than one number of times in the text.

    >The '*' means match zero or more, the group that preceeds the star can occurs any number of times in the text.

11. What is the difference between {3} and {3,5} in regular expressions?

    >{3} means match the preceeding  pattren 3 times

    > {3,5} means can match three, four, or five instances of preceeding group.  

12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

    >\d - Any numeric digit from 0 to 9

    >\w - Any letter, numeric digit, or the underscore character.

    >\s - Any space, tab, or newline character.

13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

    >\D - Any charecter that is not numeric digit from 0 to 9

    >\W - Any character that is not a letter, numeric digit, or the underscore character.

    >\S - Any character that is not a space, tab, or newline
14. What is the difference between .* and .*??

    >'.*' uses greedy mode.

    >'.*?' ises non-greedy mode 

    >'.' means anything except newline. '*' means zero or more of the preeceding character
15. What is the character class syntax to match all numbers and lowercase letters?

    >[a-z0-9]
16. How do you make a regular expression case-insensitive?

    >Passing **re.I** or **re.IGNORECASE** as the second argument to re.compile() it will make the match to case in sensitive.
17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

    >By passing **re.DOTALL** in the second aurgument to re.compile(), you can make dot character match **all characters, including the newline character**.
18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

    >numRegex = re.compile(r'\d+')

    >numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')

    output :

    >'X drummers, X pipers, five rings, X hens'
19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

    >By telling the re.compile() function to **ignore white spaces and comments inside the regular expression string**.
20. How would you write a regex that matches a number with commas for every three digits? It must match the following:

    - '42'
    - '1,234'
    - '6,368,745'

     but not the following:

    - '12,34,567' (which has only two digits between the commas)
    - '1234' (which lacks commas)

    >commaregex = re.compile(r'^\d{1,3}(,\d{3})*$')

21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

    - 'Haruto Watanabe'
    - 'Alice Watanabe'
    - 'RoboCop Watanabe'

     but not the following:

    - 'haruto Watanabe' (where the first name is not capitalized)
    - 'Mr. Watanabe' (where the preceding word has a nonletter character)
    - 'Watanabe' (which has no first name)
    - 'Haruto watanabe' (where Watanabe is not capitalized)

    >re.compile(r'[A-Z][a-z]*\sWatanabe')

22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

    - 'Alice eats apples.'
    - 'Bob pets cats.'
    - 'Carol throws baseballs.'
    - 'Alice throws Apples.'
    - 'BOB EATS CATS.'

     but not the following:

    - 'RoboCop eats apples.'
    - 'ALICE THROWS FOOTBALLS.'
    - 'Carol eats 7 cats.'

    >re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\ .' , re.I)