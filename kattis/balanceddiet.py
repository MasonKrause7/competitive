from math import inf


while True:
    
    line =  [int(x) for x in input().split()]
    n = line[0]
    if n <= 0:
        break
    cans = line[1:]

    memo = {}
    minimum_difference = inf
    candidate_solution = (0,0)

    def backtrack(curr_m1, curr_m2, index, n, cans, minimum_difference, candidate_solution):
        if index == n:
            sum1 = sum(curr_m1)
            sum2  = sum(curr_m2)
            if sum1 >= sum2 and sum1-sum2 < minimum_difference:
                minimum_difference = sum1-sum2
                candidate_solution=(sum1, sum2)
                #print(f"found a new min_diff={minimum_difference} and candidate_solution={candidate_solution} with meal1={curr_m1} and meal2={curr_m2}")
        else:
            curr_m1.append(cans[index])
            if tuple(curr_m1) in memo:
                minimum_difference = memo[tuple(curr_m1)][0]
                candidate_solution = memo[tuple(curr_m1)][1]
            else:
                minimum_difference, candidate_solution = backtrack(curr_m1, curr_m2, index+1, n, cans, minimum_difference, candidate_solution)
                memo[tuple(curr_m1)] = [minimum_difference, candidate_solution]
                curr_m1.pop(-1)
                
            curr_m2.append(cans[index])
            if tuple(curr_m2) in memo:
                minimum_difference = memo[tuple(curr_m2)][0]
                candidate_solution = memo[tuple(curr_m2)][1]
            else:
                minimum_difference,candidate_solution = backtrack(curr_m1, curr_m2, index+1, n, cans, minimum_difference, candidate_solution)
                memo[tuple(curr_m2)] = [minimum_difference, candidate_solution]
                curr_m2.pop(-1)
        return minimum_difference, candidate_solution
            
    minimum_difference, candidate_solution = backtrack([],[],0, n, cans, minimum_difference, candidate_solution)
    print(candidate_solution[0], candidate_solution[1])

        
    
    
