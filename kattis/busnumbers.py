def simplify_list(numbers):
    simplified_list = []
    start = None
    start_index = -1
    numbers.sort()
    for i in range(len(numbers)):
        if start is None:
            start = numbers[i]
            start_index = i
        elif numbers[i] == numbers[i-1] + 1:
            continue
        else:
            if start == numbers[i-1]:
                simplified_list.append(str(start))
            else:
                if i-start_index <= 2:
                    simplified_list.append(f"{start}")
                    simplified_list.append(f"{numbers[i-1]}")
                else:
                    simplified_list.append(f"{start}-{numbers[i-1]}")
            start = numbers[i]
            start_index = i
    if start is not None:
        if start == numbers[-1]:
            simplified_list.append(str(start))
        else:
            simplified_list.append(f"{start}-{numbers[-1]}")
    return simplified_list

int(input())
input_list = [int(x) for x in input().split()]
output_list = simplify_list(input_list)
print(*output_list, sep=" ")
