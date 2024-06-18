"""
CSCI-665 Assignment 5 - Stage

This is the program used to determine the minimum possible sum of height differences
from one student to the next on stage.

author: Mariam Abidi, Dhruv Dave
reference: Aaron Deever.
"""
def min_height_difference_sum(A, B):
    """
    Computes the minimum possible sum of height differences between two lists A and B.

    Args:
    A (list): List of integers representing heights.
    B (list): List of integers representing heights.

    Returns:
    int: Minimum possible sum of height differences.
    """
    n = len(A)
    m = len(B)

    # Initialize a 3-dimensional list to store minimum height differences
    S = [[[0, 0] for _ in range(m + 1)] for _ in range(n + 1)]

    # Compute minimum possible sum of height differences

    # Compute initial values for the first row
    for j in range(1, m + 1):
        S[0][j][1] = S[0][j - 1][1] + abs(B[j - 1] - B[j - 2]) if j > 1 else 0

    # Compute initial values for the first column
    for i in range(1, n + 1):
        S[i][0][0] = S[i - 1][0][0] + abs(A[i - 1] - A[i - 2]) if i > 1 else 0

        # Compute the minimum height differences for each cell
        for j in range(1, m + 1):
            if i > 1:
                S[i][j][0] = min(S[i - 1][j][0] + abs(A[i - 1] - A[i - 2]), S[i - 1][j][1] + abs(B[j - 1] - A[i - 1]))
            else:
                S[i][j][0] = S[i - 1][j][1] + abs(B[j - 1] - A[i - 1])
            if j > 2:
                S[i][j][1] = min(S[i][j - 1][1] + abs(B[j - 1] - B[j - 2]), S[i][j - 1][0] + abs(A[i - 1] - B[j - 1]))
            else:
                S[i][j][1] = S[i][j - 1][0] + abs(A[i - 1] - B[j - 1])

    return min(S[n][m][0], S[n][m][1])


def user_input():
    """
    Prompt user for input and return lists of heights.

    Returns:
    tuple: Lengths of lists A and B, and lists A and B.
    """
    list1_len = int(input())
    list2_len = int(input())
    list1 = input().split()
    list2 = input().split()

    return list1_len, list2_len, [int(char) for char in list1], [int(char) for char in list2]


def main():
    """
    Main function to execute the program.
    """
    list1_len, list2_len, list1, list2 = user_input()
    answer = min_height_difference_sum(list1, list2)
    print(answer)


if __name__ == '__main__':
    main()
