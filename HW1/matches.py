"""
matches.py
author: Mariam Abidi
        Dhruv Dave

description: An algorithm that determines if there exist two completely different stable matchings for the
given data.
"""
from typing import Any

"""
author: CS RIT
description: A linkable node class for use in stacks, queues, and linked lists
"""

class LinkedNode:
    __slots__ = "_value", "_link"
    _value: Any
    _link: 'LinkedNode'

    def __init__(self, value: Any, link: 'LinkedNode' = None) -> None:
        """ Create a new node and optionally link it to an existing one.
            param value: the value to be stored in the new node
            param link: the node linked to this one
        """
        self._value = value
        self._link = link

    def get_value(self) -> Any:
        return self._value

    def get_link(self) -> 'LinkedNode':
        return self._link

    def set_link(self, node: 'LinkedNode') -> None:
        self._link = node

    def __str__(self) -> str:
        """ Return a string representation of the contents of
            this node. The link is not included.
        """
        return str(self._value)

    def __repr__(self) -> str:
        """ Return a string that, if evaluated, would recreate
            this node and the node to which it is linked.
            This function should not be called for a circular
            list.
        """
        return "LinkedNode(" + repr(self._value) + "," + \
            repr(self._link) + ")"


"""
stack.py
author: CS RIT
description: A linked stack (LIFO) implementation
"""


class Stack:
    __slots__ = "_top"
    _top: LinkedNode

    def __init__(self) -> None:
        """ Create a new empty stack."""
        self._top = None

    def __str__(self) -> str:
        """ Return a string representation of the contents of
            this stack, top value first.
        """
        result = "Stack["
        n = self._top
        while n != None:
            result += " " + str(n.get_value())
            n = n.get_link()
        result += " ]"
        return result

    def is_empty(self) -> bool:
        return self._top == None

    def push(self, newValue: Any) -> None:
        self._top = LinkedNode(newValue, self._top)

    def pop(self) -> None:
        assert not self.is_empty(), "Pop from empty stack"
        self._top = self._top.get_link()

    def peek(self) -> Any:
        assert not self.is_empty(), "peek on empty stack"
        return self._top.get_value()

    insert = push
    remove = pop


def decision(prof_list, student_list):
    """
    This is a method which decides if the given two lists have common pairs.
    :param prof_list:
    :param student_list:
    :return:
    """
    for index in range(min(len(prof_list), len(student_list))):
        if prof_list[index] == student_list[index]:
            return "NO"
    return "YES"


def user_input():
    """
    This method defines the user input details
    :return:
    """
    n = input()
    inverse_professors = list()
    original_professors = list()
    inverse_students = list()
    original_students = list()

    for _ in range(0, int(n)):
        professor_pref = input().split()
        original_professors.append(professor_pref)
        professor_inverse = ["$"] * len(professor_pref)
        for i in range(0, len(professor_pref)):
            professor_inverse[int(professor_pref[i])] = i
        inverse_professors.append(professor_inverse)

    for _ in range(int(n), 2 * int(n)):
        student_pref = input().split()
        original_students.append(student_pref)
        students_inverse = ["$"] * len(student_pref)
        for i in range(0, len(student_pref)):
            students_inverse[int(student_pref[i])] = i
        inverse_students.append(students_inverse)

    return original_students, inverse_students, original_professors, inverse_professors


def student_stable_matching(professors, students):
    """
    This function performs the gale shapley algorithm giving the student optimal results.
    :param professors: list of professors
    :param students: list of students
    :return:
    """
    free_students = Stack()
    partnerStudent = ["$"] * len(students)
    partnerProf = ["$"] * len(professors)

    # Pushes the index values into the stack
    for i in range(len(students) - 1, -1, -1):
        free_students.push(i)

    # This is while loop that checks if there is a free student and if he has asked
    # every professor on the preference list or not
    while not free_students.is_empty() and len(professors[free_students.peek()]) != 0:
        student_index = free_students.peek()
        chosen_student = students[student_index]
        prof_to_ask = int(chosen_student[0])
        prof_list = professors[prof_to_ask]

        # Checks if the selected professor is free
        if partnerProf[prof_to_ask] == "$":
            partnerStudent[student_index] = prof_to_ask
            partnerProf[prof_to_ask] = student_index
            free_students.pop()

        # Checks if the student has higher priority or not and updates if yes
        elif prof_list[partnerProf[prof_to_ask]] > prof_list[student_index]:
            free_students.pop()
            prev_student = students[partnerProf[prof_to_ask]]
            prev_student.remove(str(prof_to_ask))
            free_students.push(partnerProf[prof_to_ask])
            partnerProf[prof_to_ask] = student_index
            partnerStudent[student_index] = prof_to_ask

        # Professor rejects the student
        else:
            free_students.pop()
            students[student_index].remove(str(prof_to_ask))
            free_students.push(student_index)

    return partnerStudent


def professor_stable_matching(professors, students):
    """
    This function performs the gale shapley algorithm giving the professor optimal results.
    :param professors: list of professors
    :param students: list of students
    :return:
    """
    free_prof = Stack()
    partnerStudent = ["$"] * len(students)
    partnerProf = ["$"] * len(professors)

    # Pushes the index values into the stack
    for i in range(len(professors) - 1, -1, -1):
        free_prof.push(i)

    # This is while loop that checks if there is a free professor and if he has asked
    # every student on the preference list or not
    while not free_prof.is_empty() and len(professors[free_prof.peek()]) != 0:
        prof_index = free_prof.peek()
        chosen_prof = professors[prof_index]
        student_to_ask = int(chosen_prof[0])
        students_list = students[student_to_ask]

        # Checks if the selected student is free
        if partnerStudent[student_to_ask] == "$":
            partnerProf[prof_index] = student_to_ask
            partnerStudent[student_to_ask] = prof_index
            free_prof.pop()

        # Checks if the professor has higher priority or not and updates if yes
        elif students_list[partnerStudent[student_to_ask]] > students_list[prof_index]:
            free_prof.pop()
            prev_prof = professors[partnerStudent[student_to_ask]]
            prev_prof.remove(str(student_to_ask))
            free_prof.push(partnerStudent[student_to_ask])
            partnerStudent[student_to_ask] = prof_index
            partnerProf[prof_index] = student_to_ask

        # Student rejects the professor
        else:
            free_prof.pop()
            professors[prof_index].remove(str(student_to_ask))
            free_prof.push(prof_index)

    return partnerStudent


def main():
    """
    The main function
    :return:
    """
    original_students, inverse_students, original_professors, inverse_professors = user_input()
    prof_list = professor_stable_matching(original_professors, inverse_students)
    student_list = student_stable_matching(inverse_professors, original_students)
    result = decision(prof_list, student_list)
    # print(prof_list)
    # print(student_list)
    print(result)


# Main Conditional Guard
if __name__ == '__main__':
    main()
