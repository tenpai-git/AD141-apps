#!/usr/bin/python3

from practice1 import Person

class Family:

    def __init__(self, parent1, parent2, *children):
        self.parent1 = parent1
        self.parent2 = parent2
        self.children = list(children)

    def add(self, child):
        self.child = self.children.append(child)

    def __str__(self):
        fmt = str()
        spacing = "\n\t"
        fmt += spacing + str(self.parent1)
        fmt += spacing + str(self.parent2)
        for offspring in self.children:
            fmt += spacing + str(offspring)
        return fmt


def main():
    mother = Person("Mom", 45, "F")
    father = Person("Dad", 45, "M")
    kid1 = Person("Johnie", 2, "M")
    kid2 = Person("Janie", 3, "F")
    myFamily = Family(mother, father, kid1, kid2)
    kid3 = Person("Paulie", 1, "M")
    myFamily.add(kid3)
    print(myFamily)

if __name__ == "__main__":
    main()
