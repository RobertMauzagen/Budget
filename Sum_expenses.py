import Balance

import matplotlib.pyplot as plt

###Function will show amount of expences by category###

def main():
    cat = Balance.Balance()
    cat.reading_balance('balance.csv')
    expences_cat = cat.clasification()
    sum_expences_cat = []

    for i in expences_cat:
        sum_expences_cat.append(sum(i))
    
    fig, ax = plt.subplots()
    
    x_axis = ['Needed','Loans', 'Food', 'Unnecessery']
    values = [sum_expences_cat[0], sum_expences_cat[1], sum_expences_cat[2], sum_expences_cat[3]]
    
    ax.bar(x_axis, values, color = ['green', 'red', 'blue', 'yellow'], edgecolor = 'black', width = 1)
    ax.set_title('Amount of expences by category')
    
    plt.show()


if __name__ == '__main__':
    main()
