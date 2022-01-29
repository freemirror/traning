class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastname(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (100 + percent)/100


John = Worker('John Doe', 50000)
Jack = Worker('Jack Daniels', 60000)
print(John.lastname(), Jack.lastname())
Jack.giveRaise(20)
print(Jack.pay, Jack.name)
John.giveRaise(-10)
print(John.pay, John.name)



L = []
if type(L) == type([]):
    print('yes')
if type(L) == list:
    print('yes')
if isinstance(L, list):
    print('yes')
