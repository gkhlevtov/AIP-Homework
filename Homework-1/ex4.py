class Result:

    def __init__(self, info):
        self.text = str(info[0] + ' ' + info[1] + ' ' + info[2])
        self.lst = []
        for i in range(3, 9):
            if info[i] == 'x':
                self.lst.append(0)
            else:
                self.lst.append(float(info[i]))

    def best_time(self):
        return sorted(self.lst, reverse=True)

    def __str__(self):
        return f'{self.text} {str(self.best_time())[1:-1]}'

    def __le__(self, other):
        return isinstance(other, Result) and self.best_time()[0] <= other.best_time()[0]


class Table:
    num = 3

    def __init__(self, number, sportlist):
        self.num = number
        self.reslist = sportlist
        self.printlist = []

    def print_table(self):
        for i in range(len(self.reslist)):
            if max(self.reslist[i].best_time) == 0:
                continue
            else:
                self.printlist.append(
                    str(i + 1) + ') ' + self.reslist[i].text + ' ' + (max(self.reslist[i].best_time())))

        if not self.printlist:
            print('No results.')
        else:
            print([x for x in self.printlist], sep='\n')


sportlist = []
n = int(input())
for i in range(8):
     sportlist.append(Result(list(input().split())))

reslist = []


for i in range(len(sportlist)):
    for k in range(6):
        if sportlist[i].best_time()[k] == sportlist[i].best_time()[k+1]:
            continue
        elif sportlist[i].best_time()[k] > sportlist[i].best_time()[k+1]:
            reslist.append()



#srtlist = sorted(list([float(x.best_time()[0]) for x in sportlist]))
#print(srtlist)
#res = Result(list(input().split()))
#print(res)
# Tbl = Table(3, sportlist)
# print(Table.print_table())

