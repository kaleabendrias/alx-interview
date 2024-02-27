# Making Change

## Description
Given a pile of coins of different values, the task is to determine the fewest number of coins needed to meet a given total amount. The function `makeChange(coins, total)` takes in a list of coin values `coins` and a target total amount `total`. It returns the fewest number of coins needed to meet the total. If the total is 0 or less, it returns 0. If the total cannot be met by any combination of the given coins, it returns -1.

## Prototype
```python
def makeChange(coins, total)
```

## Parameters
- `coins`: A list of the values of the coins in your possession.
  - The value of a coin will always be an integer greater than 0.
  - You can assume you have an infinite number of each denomination of coin in the list.
- `total`: The target total amount to be met.

## Return
- The fewest number of coins needed to meet the total amount.
- If the total is 0 or less, return 0.
- If the total cannot be met by any number of coins you have, return -1.

## Examples
```python
print(makeChange([1, 2, 25], 37))  # Output: 7

print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Evaluation
Your solution's runtime will be evaluated in this task.