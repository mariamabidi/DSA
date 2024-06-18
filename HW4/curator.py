def counting_sort(arr, exp):
    """
    Counting sort implementation for sorting items based on their category.

    Parameters:
        arr (list): List of items to be sorted.
        exp (int): Current exponent for sorting based on digit place.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit at the current exponent place
    for i in range(n):
        index = arr[i][2] // exp % 10
        count[index] += 1

    # Modify count array to store actual position of each digit in output
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i][2] // exp % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def sort_items(items):
    """
    Sort items based on their category and previous items in that category.

    Parameters:
        items (list): List of items where each item is represented as a list of integers.

    Returns:
        list: Sorted list of items.
    """
    max_val = max(items, key=lambda x: x[2])[2]
    exp = 1

    # Perform counting sort for each digit place
    while max_val // exp > 0:
        counting_sort(items, exp)
        exp *= 10

    prev_list = [0]*len(items)

    # Calculate the number of previous items in each category
    for item in items:
        item_cat = item[-1]
        prev_list[item_cat] += 1

    # Add the number of previous items in each category to the items
    for item in items:
        item_category = item[-1]
        num = 0
        for i in range(item_category):
            num += prev_list[i]
        item.append(num)

    return items


def curator(total_items, total_budget, sorted_items):
    """
    Curator function to find the maximum value of items that can be bought within the given budget.

    Parameters:
        total_items (int): Total number of items available.
        total_budget (int): Total budget available.
        sorted_items (list): List of sorted items.

    Returns:
        int: Maximum value of items that can be bought within the budget.
    """
    # Initialize dynamic programming table
    dp = [[0] * (total_budget + 1) for _ in range(total_items + 1)]

    # Fill the dynamic programming table
    for j in range(len(dp)):
        for v in range(len(dp[j])):
            if j == 0 or v == 0:
                dp[j][v] = 0
            else:
                item = sorted_items[j-1]
                m = v-item[0]
                if m >= 0:
                    dp[j][v] = max(dp[j-1][v], (item[1] + dp[item[3]][v-item[0]]))
                else:
                    dp[j][v] = dp[j-1][v]

    return dp[total_items][total_budget]


def main(input_file):
    """
    Main function to read input from a file and call other functions.

    Parameters:
        input_file (str): Path to the input file.
    """
    with open(input_file, 'r') as file:
        total_items = int(file.readline().strip())
        total_budget = int(file.readline().strip())
        items = []

        # Input items
        for _ in range(total_items):
            item = list(map(int, file.readline().strip().split()))
            items.append(item)

    # Sort the items based on category and previous items in that category
    sorted_items = sort_items(items)

    # Find the maximum value of items that can be bought within the budget
    answer = curator(total_items, total_budget, sorted_items)
    print(answer)


# Main Conditional Guard
if __name__ == "__main__":
    input_file = "m.txt"
    main(input_file)

