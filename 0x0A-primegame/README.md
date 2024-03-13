# Prime Game

## Description

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

This Python script `prime_game.py` provides a solution to determine the winner of multiple rounds of this game. It defines functions to check if a number is prime, generate a list of prime numbers up to a given limit, and simulate the game for each round.

## Usage

### Prerequisites

- Python 3.x

### Running the Script

1. Clone the repository or download the `prime_game.py` file.
2. Open a terminal and navigate to the directory containing `prime_game.py`.
3. Run the script with Python:

   ```bash
   ./main_0.py
   ```

4. The script will output the winner of the game based on the provided rounds and values of `n`.

### Function Description

- `is_prime(num)`: Checks if a number is prime.
- `primes_up_to_n(n)`: Generates a list of prime numbers up to `n`.
- `isWinner(x, nums)`: Determines the winner of the game for multiple rounds.

## Example

Output:

```bash
Winner: Ben
```

## Author

- [Kaleab Endrias]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
