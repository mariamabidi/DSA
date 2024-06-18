"""
morseVowel.py
author: Mariam Abidi
        Dhruv Dave

description: An algorithm that computes the number of possible letter sequences containing only vowels (A,E,I,O,U) that
can be derived from a given input sequence of dots and dashes of length n.
"""


def countVowelSequences(sequence):
    """
    Count the number of possible sequences containing only vowels (A, E, I, O, U)
    that can be derived from a given input sequence of dots (.) and dashes (-).
    :param sequence: The input sequence of dots and dashes.
    :return: The number of possible sequences containing only vowels.
    """
    # Get the length of the input sequence
    n = len(sequence)

    # Initialize a list to store counts of possible sequences
    the_list = [0] * (n + 1)
    the_list[0] = 1

    # Iterate through the sequence
    for i in range(len(sequence)):
        if sequence[0] == "-":
            return 0  # If the sequence starts with a dash, no valid sequences
        elif sequence[i] == ".":
            # Extend the sequence with a vowel (A, E, I, O, U)
            the_list[i + 1] += the_list[i]
            # If the previous character is also a dot, extend the sequence further
            if sequence[i - 1] == ".":
                the_list[i + 1] += the_list[i - 1]
        elif sequence[i] == "-":  # Handle dash (-)
            if sequence[i - 1] == ".":  # If the previous character is a dot
                the_list[i + 1] += the_list[i - 1]
                if sequence[i - 2] == ".":  # If two characters ago was also a dot
                    the_list[i + 1] += the_list[i - 2]
            if sequence[i - 1] == "-":  # If the previous character is a dash
                if sequence[i - 2] == "-":  # If two characters ago was also a dash
                    the_list[i + 1] += the_list[i - 2]

    # Return the count of possible sequences up to the nth character
    return the_list[n]


def main():
    """
        Main function to handle user input and call countVowelSequences function.
    """
    no_of_char = input()
    sequence = input()
    result = countVowelSequences(sequence)
    print(result)


# Main Conditional Guard
if __name__ == '__main__':
    main()
