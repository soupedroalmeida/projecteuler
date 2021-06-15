unities = [3, 3, 5, 4, 4, 3, 5, 5, 4]
u_zero = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
uz_teens = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [6, 6, 5, 5, 5, 7, 6, 6]

unities_ten = list()
for t in tens:
    for uz in u_zero:
        unities_ten.append(t + uz)

unities_hundred = list()
for u in unities:
    unities_hundred.append(u + 7)

uh_teens = list()
for uh in unities_hundred:
    for uzt in uz_teens:
        if uzt == 0: uh_teens.append(uh)
        else: uh_teens.append(uh + 3 + uzt)

uh_tens = list()
for uh in unities_hundred:
    for t in tens:
        uh_tens.append(uh + 3 + t)

uht_unities = list()
for uht in uh_tens:
    for uz in u_zero:
        uht_unities.append(uht + uz)

result = sum(uz_teens) + sum(unities_ten) + sum(uh_teens) + sum(uht_unities) + 11
print(result)
