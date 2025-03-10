def findIntervals(x, left, right) -> []:
    global a
    indeces = [index+left for index, elem in enumerate(a[left:right]) if elem == x]
    print(f"indeces of {x} in {a[left:right]} == {indeces}")
    intervals = []
    if indeces:
        if left != indeces[0]:
            
            intervals.append((left, indeces[0]))
        if len(indeces) > 1:
            for i in range(1, len(indeces)):
                if len(intervals)>0:
                    interval = (intervals[i-2][1], indeces[i])
                else:
                    interval = (left, indeces[i])
                intervals.append(interval)
                
        if indeces[len(indeces)-1]!=right and x==0:
            intervals.append((indeces[len(indeces)-1], right))
        elif indeces[len(indeces)-1]!=right-1:
            intervals.append((indeces[-1],right-1))
    else:
        intervals.append((left,right))
    
    print(f"INTERVALS of {x} in {a[left:right]} = {intervals}")
    return intervals
    
def dp(left, right):#returns cost to make a[left:right+1]
    print(f"DP: left={left}={a[left]}, right={right}={a[right]}")
    if right-left <= 0:
        if a[left] == 0:
            print(f"right-left<=0, and a[left]==0, returning 0")
            return 0
        else:
            print(f"right-left<=0, but a[left]!=0, returning 1")
            return 1
    elif right-left == 1:
        if a[left] == a[right]:
            if a[left] == 0:
                print(f"right-left==1, and a[left]==a[right], and both == 0, returning 0")
                return 0
            else:
                print(f"right-left==1, and a[left]==a[right], but they are not == 0, so returning 1")
                return 1
        elif a[left] == 0 or a[right] == 0:
            print(f"right-left==1, and a[left]!=a[right], but one of them is 0, so returning 1")
            return 1
        else:
            print(f"right-left==1, and a[left]!=a[right], neither of them are 0, so returning 0, because elevation_change will add 1 for each change")
            return 0
    else:
        print(f"there was separation between right and left")
        total_cost = 0
        x = a[left+1]
        elevation_raises = 0
        if x > 0:
            elevation_raises = 1
        print(f"x={x}, elevation_raises={elevation_raises}")
        if x in a[left+2:right]:
            intervals = findIntervals(x,left+1,right)
            for interval in intervals:
                cost_of_interval = dp(interval[0], interval[1])
                print(f"cost_of_interval ({interval[0]},{interval[1]}) == {cost_of_interval}")
                total_cost += cost_of_interval
            total_cost += elevation_raises
            print(f"total_cost + elevation_raises for x={x} is {total_cost}")
        else:
            print(f"x={x} was not found in {a[left+2:right]}")
            cost_of_remaining = dp(left+1, right)
            print(f"cost_of_remaining in the interval ({left+1},{right}) is {cost_of_remaining}")
            total_cost+=cost_of_remaining
            total_cost += elevation_raises
            print(f"total_cost + elevation_raises for x={x} is {total_cost}")
        return total_cost
    


n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

intervals_of_zero = findIntervals(0, 0, len(a)-1)

total_edits = 0
for interval in intervals_of_zero:
    sum_of_edits_to_make_interval = dp(interval[0], interval[1])
    total_edits += sum_of_edits_to_make_interval
    print(f"num_edits for interval ({interval[0]},{interval[1]}) is {sum_of_edits_to_make_interval}")
    print(f"adding that to total_edits yields {total_edits} edits so far")
print(total_edits)

