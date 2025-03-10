


while True:
    try:
        line = input().split()
        name = ""
        rates = []
        for entry in line:
            try:
                rate = float(entry)
                rates.append(rate)
            except:
                name += entry+" "
        s = sum(rates)
        a = s/len(rates)
        print(a, name)
    except:
        break

