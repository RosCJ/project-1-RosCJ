# Author: Crystal Ros
# Date: April 10, 2020
# Description: This program creates a class called Person with two private data members, name and age. The class has an
# init method that initializes the Person's name and age. It has a get_age method. A separate function called basic_
# stats takes a list of the age of each Person in the person list.  This program imports the statistics module to find
# the mean, median, and mode of the age of the Person objects.

import statistics


class Person:
    """Represents a Person."""
    def __init__(self, name, age):
        """Creates a Person object with the specified name and age."""
        self._name = name
        self._age = age

    def get_age(self):
        """Returns the age of the person"""
        return self._age


# p1 = Person("Kay", 73)
# p2 = Person("Mercedes", 24)
# p3 = Person("Ava", 48)
# p4 = Person("Marta", 24)

# person_list = [p1, p2, p3, p4]


def basic_stats(person_list):
    age_list = [person.get_age() for person in person_list]    # Creates a list of ages
    print(age_list)
    x = statistics.mean(age_list)
    y = statistics.median(age_list)
    z = statistics.mode(age_list)
    result = (x, y, z)
    return result


# print(basic_stats(person_list))
