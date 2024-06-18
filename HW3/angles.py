def count_right_triangles(points):
    n = len(points)
    if n < 3:
        return 0

    triangles_count = 0

    for i in range(n):
        slopes = {}

        for j in range(n):
            if i != j:
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx != 0:
                    slope = dy / dx
                else:
                    slope = float('inf')

                if slope not in slopes:
                    slopes[slope] = []

                slopes[slope].append((dx * dx + dy * dy, j))

        for slope, sorted_points in slopes.items():
            sorted_points.sort()

            k = len(sorted_points)
            if k < 2:
                continue

            count = 0
            for p in range(k):
                for q in range(p + 1, k):
                    d1, d2 = sorted_points[p][0], sorted_points[q][0]
                    if d1 + d2 == sorted_points[-1][0]:
                        count += 1

            triangles_count += count

    return triangles_count // 2  # Each triangle is counted twice, once for each end of the hypotenuse

def take_coordinates_input():
    points = []
    num_points = int(input())
    for _ in range(num_points):
        x, y = map(int, input().split())
        points.append((x, y))
    return points


def main():
    """
        Main function to handle user input and call countVowelSequences function.
    """
    points = take_coordinates_input()
    result = count_right_triangles(points)
    print(result)


# Main Conditional Guard
if __name__ == '__main__':
    main()
