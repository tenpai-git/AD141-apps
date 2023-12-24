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

    def __eq__(self, obj):
        if type(obj) != Family:
           return False
        else:
            if len(self.children) == len(obj.children):
                return True

    def __gt__(self, obj):
        if type(obj) != Family:
           return False
        else:
            if len(self.children) > len(obj.children):
                return True

    def __lt__(self, obj):
        if type(obj) != Family:
           return False
        else:
            if len(self.children) < len(obj.children):
                return True

def main():
    mom = Person("Mom", 45, "F")
    dad = Person("Dad", 45, "M")
    kid1 = Person("Johnie", 2, "M")
    kid2 = Person("Janie", 3, "F")
    kid3 = Person("Timmy", 5, "M")

#AD141 Test Conditions
    myFamily = Family(mom, dad, kid1, kid2)
    smiths = Family(mom, dad, kid1, kid2, kid3)
    if (myFamily > smiths):
        print("we have more kids than smiths")
    if (myFamily == smiths):
        print("families have same # of kids")
    if (myFamily < smiths):
        print("we have fewer kids than smiths")

if __name__ == "__main__":
    main()
