import Balance

import collections
import matplotlib.pyplot as plt

###Function will show most common expences###

def main():
    common = Balance.Balance()
    common.reading_balance('balance.csv')
    often_used = []

    for i in common.expences:
        often_used.append(i.category)

    counter = collections.Counter(often_used)
    most_counted = counter.most_common(3)
    category, amount = zip(*most_counted)
    
    fig, ax = plt.subplots()

    ax.bar(category, amount, color = ['green', 'red', 'blue'], edgecolor = 'black', width = 1)
    ax.set_title('the amount of purchases by category.')

    plt.show()


if __name__ == '__main__':
    main()