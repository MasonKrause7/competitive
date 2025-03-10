num_friends, days_til_bday, today = [int(x) for x in input().split()]

num_friends_that_will_make_it = 0
for i in range(num_friends):
    day_into_quarantine = int(input())
    if day_into_quarantine + 14 <= today + days_til_bday:
        num_friends_that_will_make_it += 1

print(num_friends_that_will_make_it)

