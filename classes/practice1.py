#!/usr/bin/python3

class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        fmt = "Name: {} Age: {} Gender {}"
        return fmt.format(self.name, self.age, self.gender)

def main():
   p1 = Person("Michael", 45, "M")
   print(p1)

if __name__ == "__main__":
   main()
