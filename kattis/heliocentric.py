case_num = 1
while True:
    try:
        se, sm = [int(x) for x in input().split()]
        if se == 0 and sm == 0:
            print(f"Case {case_num}: 0")
            case_num += 1
            continue
        earth_0_days = [365-se]
        mars_0_days = [687-sm]

        earth_day = earth_0_days[0]

        i = 1
        while earth_day not in mars_0_days:
            mars_0_days.append((687-sm)+(687*i))
            earth_day = (365-se)+(365*i)
            earth_0_days.append(earth_day)
            i += 1

        print(f"Case {case_num}: {earth_0_days[-1]}")
        case_num += 1
    except:
        break
            

        
