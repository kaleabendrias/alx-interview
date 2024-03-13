#!/usr/bin/python3
"""Maria and Ben are playing a game. Given a set of consecutive
integers starting from 1 up to and including n, they take turns choosing a
prime number from the set and removing that number and its multiples from
the set. The player that cannot make a move loses the game.
"""


def is_prime(num):
    """Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def primes_up_to_n(n):
    """Generate a list of prime numbers up to n.

    Args:
        n (int): The upper limit.

    Returns:
        list of int: A list of prime numbers up to n.
    """
    primes = []
    for i in range(1, n+1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """Check who wins the most rounds in a game of removing primes
    from consecutive integers.

    Args:
        x (int): The number of rounds.
        nums (list of int): An array of n for each round.

    Returns:
        str or None: The name of the player that won the most rounds.
        If the winner cannot be determined, returns None.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = primes_up_to_n(n)
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
