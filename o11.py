'''
In the kingdom of Numerica, there's a mystical gatekeeper named Arithmos who guards the entrance to the Royal Garden. Arithmos has a unique ability to distinguish between positive and negative magical energy associated with numbers.
Your task is to create a magical algorithm to determine whether a given number possesses positive or negative magical energy based on the ancient modulo operation. Simply you can print"Even" or "Odd" based on the given input.

Input: The input consists of a single integer, `n` (-10^9 ≤ n ≤ 10^9), representing the mystical number.

Output: Your mission is to output a message declaring whether the given number is "Even" or "Odd" based on the magical rules set by Arithmos.

Example:
Input:
14

Output:
Even

'''

#========== User's Code Starts Here ==========
def check_magical_energy(n):
    return "Even" if n % 2 == 0 else "Odd"

def main():
    n = int(input())
    print(check_magical_energy)


#========== User's Code Ends Here ==========
