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

class Manager(Worker):

    def __init__(self, name, salary, years_worked):
        super().__init__(name, salary, years_worked)
#        self.years_worked = worker.years_worked
#        self.salary = worker.salary

    def pension(self):
        return self.years_worked * (self.salary*0.20)

class Executive(Worker):

    def __init__(self, name, salary, years_worked):
        super().__init__(name, salary, years_worked)
#        self.years_worked = worker.years_worked
#        self.salary = worker.salary

    def pension(self):
        return self.years_worked * (self.salary*0.30)

def main():
    joe_worker = Worker("Joe", 250000, 5)
    manager_jane = Manager("Jane", 250000, 5)
    executive_smith = Executive("Smith", 250000, 5)
#    manager_joe = Manager(joe_worker)
#    executive_joe = Executive(joe_worker)
    print("Base Pay: " + str(joe_worker.pension()))
    print("Manager Pay: " + str(manager_jane.pension()))
    print("Executive Pay: " + str(executive_smith.pension()))

if __name__ == "__main__":
    main()
