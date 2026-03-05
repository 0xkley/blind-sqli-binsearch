# 🤖 - Blind-SQLi-BinSearch
This is a script to make automated Blind Boolean SQL Injection attacks. The script uses the Binary Search algorithm to reduce the number of "trys" to get a character or value from a field.


## Binary Search benefits
When we're looking for the character of some field, we should compare that field with every character possible, for example:

```py
character = 'M';

character == 'a'; # false
character == 'A'; # false
...
...
character == 'm'; # false
character == 'M'; # true
```

However, this can be tedious because we would need to compare every single character (and number if its necessary) manually with the field until we get the correct one, so the number of comparisons becomes much higher than when using binary search.

Binary Search is an algorithm that split the range of 2 numbers (example: 1 - 100 = 50), getting the "mid" (50) and comparing that mid the character.

If we need, for example, find the "M", the ASCII code for "M" is 77.

The range would be: 32 - 126, as these are the ASCII codes for characters from a-Z and 0-9.

So, binary search splits 32 + 126, getting the mid value: 79


```py
character = 'M';

character = 'a'; # false
character = 'A'; # false
character = 'b'; # false
...
```
