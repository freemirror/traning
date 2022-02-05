class Run:
    def __init__(self, numb,numb_2):
        self.numb = numb
        self.numb_2 = numb_2
    def summ(self):
        summa = self.numb + self.numb_2
        return summa

class Run2(Run):
    def print_summ(self):
        summako = self.summ()
        return print(summako)


first = Run(numb=23,
            numb_2=5435)
second = Run2(numb=653,
              numb_2=46535)
second.print_summ()