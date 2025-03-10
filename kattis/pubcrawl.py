n = int (input())

pubs = {}
max_q_time = 0
for i in range(n):
    name, k, t = input().split()

    pubs[name] = (int(k),int(t))
    q_time = (int(k) * int(t)) + int(t)

    if q_time > max_q_time:
        max_q_time = q_time

     
    
for pub in pubs.keys():
    k,t = pubs[pub]
    if (k*t)+t == max_q_time:
        print(pub, max_q_time)
        break




