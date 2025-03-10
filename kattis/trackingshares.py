C = int(input())

ds = {}
days = []
for c in range(C):
    ds[c]= []
    k = int(input())

    for i in range(k):
        n, d = [int(x) for x in input().split()]
        days.append(d)
        ds[c].append((d, n))
days = set(days)
days = list(days)
days.sort()

for i in range(len(days)):
    
    day = days[i]
    #whats the n from each company that had a date less than or eq to today
    shares_on_day = 0
    for c in range(C):
        greatest_day_under_today = None
        shares_from_this_c = 0
        for r in ds[c]:
            if r[0] <= day:
                if not greatest_day_under_today:
                    greatest_day_under_today = r[0]
                    shares_from_this_c = r[1]
                else:
                    if r[0] > greatest_day_under_today:
                        greatest_day_under_today = r[0]         
                        shares_from_this_c = r[1]
        shares_on_day +=shares_from_this_c
        shares_from_this_c == 0
        
    print(shares_on_day, end=" ")
            
    
            

            
            
            
        
