condition = list(map(int, input().split(' ')))

card_num = condition[0]
dealer_num = condition[1]

cards = list(map(int, input().split(' ')))
chosen_sum = 0

for i in range(0, card_num - 2):
    for j in range(i+1, card_num - 1):
        for k in range(j+1, card_num):
            if chosen_sum == 0:
                chosen_sum = cards[i] + cards[j] + cards[k]
            else:
                if abs(dealer_num - chosen_sum) > abs(dealer_num - (cards[i] + cards[j] + cards[k])) and cards[i] + cards[j] + cards[k] <= dealer_num:
                    chosen_sum = cards[i] + cards[j] + cards[k]

print(chosen_sum)
