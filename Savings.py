import Balance

import matplotlib.pyplot as plt

###Function will show budget, expences and savings###

def main():
    savings = Balance.Balance()
    savings.reading_balance('balance.csv')
    
    fig, ax = plt.subplots()
    
    x_axis = ['Budget','Expences', 'Savings',]
    values = [savings.sum_incomes, savings.sum_expences, (savings.sum_incomes - savings.sum_expences)]
    
    ax.bar(x_axis, values, color = ['green', 'red', 'blue'], edgecolor = 'black', width = 1)
    ax.set_title('Budget, expences and savings.')
    
    plt.show()


if __name__ == '__main__':
    main()