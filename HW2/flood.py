"""
flood.py
author: Mariam Abidi
        Dhruv Dave

description: Algorithm to determine if you will be able to fix all the cracks
in the dam without the village being forced to evacuate.
"""
import heapq


# Define a MaxHeap class using heapq to represent a max heap
class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, -val)

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0] if self.heap else None

    def __len__(self):
        return len(self.heap)

    def __iter__(self):
        return iter([-x for x in self.heap])

    # Decrement all elements in the heap by 1
    def increment_all(self):
        for i in range(len(self.heap)):
            self.heap[i] -= 1


# Function to get user input for the program
def user_input():
    """
    Get user input for the flooding simulation.
    :return: Tuple containing the number of cracks, threshold, water drained,
      and a list of crack information.
    """
    number_of_cracks = int(input())
    threshold = int(input())
    water_drained = int(input())
    cracks = list()

    # Read crack information from the user
    for _ in range(number_of_cracks):
        cracks.append(input().strip().split())

    return number_of_cracks, threshold, water_drained, cracks


# Function to simulate the flooding scenario
def the_flooding(number_of_cracks, threshold, water_drained, cracks):
    """
    Simulate the flooding scenario and print the result.
    :param number_of_cracks: Number of cracks in the simulation.
    :param threshold: Water level threshold for flooding.
    :param water_drained: Amount of water drained in each time step.
    :param cracks:  List of tuples representing crack information.
    :return: Result of the simulation, either "FLOOD" or "SAFE" and the maximum water level.
    """
    # Initialize a MaxHeap to track the water levels
    flooding_heap = MaxHeap()

    # Make a copy of the cracks list to keep track of the original input
    cracks_copy = cracks.copy()

    # Variables to track the state of the simulation
    cracks_fixed = 0
    max_water_level = 0
    total_water = 0
    crack_counter = 0
    m = 0

    # Continue simulation until all cracks are fixed
    while cracks_fixed < number_of_cracks:
        # Process cracks at the current time step
        while crack_counter < len(cracks) and cracks[crack_counter][0] == str(m):
            total_water += int(cracks[crack_counter][1])
            flooding_heap.push(int(cracks[crack_counter][1]))
            cracks_copy.remove(cracks[crack_counter])
            crack_counter += 1

        # Check for cracks to be removed due to draining water
        if flooding_heap.peek() is not None:
            popped_crack = flooding_heap.pop()
            total_water -= water_drained + popped_crack
            cracks_fixed += 1
        else:
            total_water -= water_drained

        # Ensure total water level is non-negative
        if total_water < 0:
            total_water = 0

        # Update the maximum water level
        if total_water > max_water_level:
            max_water_level = total_water

        # Check if the threshold is reached, and print the result
        if total_water >= threshold:
            print("FLOOD")
            print(m)
            print(total_water)
            exit(1)

        # Increment all values in the heap and update the total water
        flooding_heap.increment_all()
        for value in flooding_heap:
            total_water += value

        # Update the time step based on the remaining cracks
        if total_water == 0 and len(cracks_copy) != 0:
            m = int(cracks_copy[0][0])
        else:
            m += 1

    # If the heap is empty, print "SAFE" and the maximum water level
    if flooding_heap.peek() is None:
        print("SAFE")
        print(max_water_level)


# Main function to execute the program
def main():
    """
    Main function to execute the flooding simulation.
    """
    number_of_cracks, threshold, water_drained, cracks = user_input()
    the_flooding(number_of_cracks, threshold, water_drained, cracks)


# Main Conditional Guard
if __name__ == '__main__':
    main()
