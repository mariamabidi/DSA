def longest_path(m, n, mountain):
    """
    Finds the length of the longest decreasing path in a 2D matrix.

    Args:
        m (int): Number of rows in the matrix.
        n (int): Number of columns in the matrix.
        mountain (List[List[int]]): 2D matrix representing the terrain.

    Returns:
        int: Length of the longest decreasing path.
    """
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1),
                  (-1, 1)]

    def dfs(i, j, dp):
        """
        Depth-first search to find the longest decreasing path starting from (i, j).

        Args:
            i (int): Row index.
            j (int): Column index.
            dp (List[List[int]]): Memoization table.

        Returns:
            int: Length of the longest decreasing path starting from (i, j).
        """
        if dp[i][j] != 0:
            return dp[i][j]

        max_length = 1
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and mountain[x][y] < mountain[i][j]:
                max_length = max(max_length, 1 + dfs(x, y, dp))

        dp[i][j] = max_length
        return max_length

    max_path_length = 0
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            max_path_length = max(max_path_length, dfs(i, j, dp))

    return max_path_length


def main():
    """
    Main function to take input and print the result.
    """
    m = int(input())
    n = int(input())
    mountain = []
    for _ in range(m):
        row = list(map(int, input().split()))
        mountain.append(row)

    # Finding the longest path
    result = longest_path(m, n, mountain)
    print(result - 1)


if __name__ == '__main__':
    main()
