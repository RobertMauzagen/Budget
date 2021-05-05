import csv
from datetime import datetime

class Account():
    def __init__(self, date_string, company, category, amount):
        self.date = datetime.strptime(date_string, '%d.%m.%Y')
        self.company = company
        self.category = category
        self.amount = amount


###Class will classify our balance###

class Balance():
    def __init__(self):
        self.expences = []
        self.sum_expences = 0
        self.incomes = []
        self.sum_incomes = 0
    
    ###Reading account balance###

    def reading_balance(self, data):
        with open(data, 'r') as csvf:
            csvr = csv.reader(csvf, delimiter=';')
            for row in csvr:
                if '-' in row[3]:
                    amount = float((row[3][1:]).replace(',', '.'))
                    self.expences.append(Account(row[0], row[1], row[2], amount))
                    self.sum_expences += amount
                else:
                    amount = float(row[3].replace(',', '.'))
                    self.incomes.append(Account(row[0], row[1], row[2], amount))
                    self.sum_incomes += amount

    ###classify your spendings###

    def clasification(self):
        needed = []
        loans = []
        food = []
        unnecessary = []
        
        for x in self.expences:
            if (x.category == 'TV' or x.category == 'GAS'):
                needed.append(x.amount)
            elif x.category == 'LOAN':
                loans.append(x.amount)
            elif (x.category == 'FOOD' or x.category == 'GROCERIES'):
                food.append(x.amount)
            else:
                unnecessary.append(x.amount)
        
        return [needed, loans, food, unnecessary]  
