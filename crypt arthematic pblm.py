import itertools

def is_valid_solution(words, solution):
    # Map letters to corresponding digits based on the current solution
    letter_to_digit = {letter: digit for letter, digit in zip(solution['letters'], solution['digits'])}
    
    # Replace letters in each word with corresponding digits and convert to integer
    numbers = [int(''.join(str(letter_to_digit[letter]) for letter in word)) for word in words]
    
    # Check if the sum of the first two numbers equals the third
    return numbers[0] + numbers[1] == numbers[2]

def solve_cryptarithmetic(words):
    letters = set(''.join(words))
    if len(letters) > 10:
        raise ValueError("Too many unique letters for a valid solution.")
    
    # Generate all possible permutations of digits (0-9) for the letters
    for perm in itertools.permutations(range(10), len(letters)):
        solution = {'letters': list(letters), 'digits': perm}
        if is_valid_solution(words, solution):
            return {letter: digit for letter, digit in zip(solution['letters'], solution['digits'])}
    
    return None

def main():
    words = ["SEND", "MORE", "MONEY"]
    solution = solve_cryptarithmetic(words)
    
    if solution:
        print("Solution found:")
        for letter, digit in solution.items():
            print(f"{letter} = {digit}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()