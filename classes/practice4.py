#!/usr/bin/python3

class Worker:

    def __init__(self, name, salary, years_worked):
        self.name = name
        self.salary = salary
        self.years_worked = years_worked

    def pension(self):
        return self.years_worked * (self.salary*0.10)

    def __repr__(self):
        return self.name

class Manager:

    def __init__(self, worker):
        self.years_worked = worker.years_worked
        self.salary = worker.salary

    def pension(self):
        return self.years_worked * (self.salary*0.20)

class Executive:

    def __init__(self, worker):
        self.years_worked = worker.years_worked
        self.salary = worker.salary

    def pension(self):
        return self.years_worked * (self.salary*0.30)

def main():
    joe_worker = Worker("Joe", 250000, 5)
    manager_joe = Manager(joe_worker)
    executive_joe = Executive(joe_worker)
    print("Base Pay: " + str(joe_worker.pension()))
    print("Manager Pay: " + str(manager_joe.pension()))
    print("Executive Pay: " + str(executive_joe.pension()))

if __name__ == "__main__":
    main()
