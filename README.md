# Blind-SQLi-BinSearch
Automated Blind Boolean SQL Injection script that uses Binary Search to efficiently extract data from a vulnerable field.


# Overview
This script automates data extraction in Blind Boolean SQL Injection scenarios by reducing the number of requests needed per character using a binary search approach.


## What the script does
- Extracts data from a vulnerable field using Blind Boolean SQL Injection
- Uses binary search to reduce the number of requests per character
- Automatically iterates over positions to reconstruct full values


## Why this matters
Without binary search:
~95 requests per character

With binary search:
~7 requests per character

This drastically reduces attack time and noise.

## How Binary Search improves extraction
When extracting a character, a naive approach would compare it against every possible value:

```py
character = 'M';
character == 'a'; # false
character == 'A'; # false
...
...
character == 'm'; # false
character == 'M'; # true
```

This is inefficient because it requires checking each possible character sequentially.

## Binary Search approach

Instead of testing all values, we split the search space in half each time.
For example, suppose we want to find the character 'M' (ASCII 77).

We assume the value is within the printable ASCII range: **32 - 126**

### Step 1: Calculate midpoint 

`(32 + 126) / 2 = 79`

### Step 2: Compare midpoint with target

- If mid is higher than target (our case), this means we've gone beyond the valid search range, because the value is lower, so we reduce the range to mid - 1, not 126. So our range will be 32 - 78.
- If mid is lower than target (for example, 75), this means we've gone below the target, so it doesn't make sense to keep searching in the lower values. Because of that, we move the start of the range to mid + 1. So the new range would be 76 - 126.

We repeat the process with our current range:

```py
(32 + 78) / 2 = 55
```
Now: *55 < 77*

So the character must be in the upper half, and the new range becomes: **56 – 78**

This process continues until the exact ASCII value is found.

By repeatedly halving the search space, binary search drastically reduces the number of comparisons needed. Instead of testing every possible character sequentially, we can determine the correct value in log₂(n) steps, making the extraction process significantly faster.

## Concepts applied
- Binary Search (algorithm optimization)
- ASCII-based data extraction
- Blind Boolean SQL Injection
- HTTP request automation

## Disclaimer
This script was developed specifically for the 
[PortSwigger Web Academy](https://portswigger.net/web-security) 
Blind Boolean SQLi lab. This is not a general-purpose tool
certain parameters like cookies and endpoint URLs are 
hardcoded for that environment and would need to be adapted 
for other targets.

This script was built for educational purposes in a 
controlled lab environment.
