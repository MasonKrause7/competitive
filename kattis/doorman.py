x = int(input())

q = list(input())
num_men=0
num_women = 0
diff = 0
total = 0


while len(q) > 1 and diff <= x:
    #print(q)
    if num_men == num_women:
        let_in = q.pop(0)
        total += 1
        #print(let_in)
        if let_in == 'M':
            num_men += 1
        else:
            num_women += 1
        diff = abs(num_men-num_women)
        #print(diff)
        continue
    if num_men > num_women:
        if q[0] == 'M':
            let_in = q.pop(1)
            total += 1
            #print(let_in)
            if let_in == 'M':
                num_men+=1
            else:
                num_women+=1
        
        else:
            let_in = q.pop(0)
            total += 1
            num_women+=1
    else:
        if q[0] == 'W':
            let_in = q.pop(1)
            total += 1
            if let_in == 'M':
                num_men+=1
            else:
                num_women+=1
        else:
            let_in = q.pop(0)
            total += 1
            num_men += 1
        #print(let_in)
    diff = abs(num_men - num_women)
    #print(f"diff={diff}")

if diff > x:
    print(total-1)
else:
    if diff+1 > x:
        print(total)
    else:
        print(total+1)
