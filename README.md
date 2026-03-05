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
For example, supose we want to find the character "M", whose ASCII code is 77.
The range would be: 32 - 126, as these are the ASCII codes for characters from a-Z and 0-9.
If we assume the character is within the printable ASCII range, the search space would be 32 - 126
Binary search first calculates the midpoint: `(32 + 126) / 2 = 79`
Now we compare 79 with the target value 77:
If the value is greater than 77, the character must be in the lower half of the range.
If the value is less than 77, the character must be in the upper half of the range.
Since 79 > 77, we discard the upper half and keep the new range: *32 – 79*
We repeat the process:
```py
(32 + 79) / 2 = 55
```
Now: *55 < 77*
So the character must be in the upper half, and the new range becomes: *55 – 79*
This process continues until the exact ASCII value is found.
By repeatedly halving the search space, binary search drastically reduces the number of comparisons needed. Instead of testing every possible character sequentially, we can determine the correct value in log₂(n) steps, making the extraction process significantly faster.

## ⚠️ Disclaimer
This script was developed specifically for the 
[PortSwigger Web Academy](https://portswigger.net/web-security) 
Blind Boolean SQLi lab. This is not a general-purpose tool
certain parameters like cookies and endpoint URLs are 
hardcoded for that environment and would need to be adapted 
for other targets.

This script was built for educational purposes in a 
controlled lab environment.
