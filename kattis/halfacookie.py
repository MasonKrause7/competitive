while True:
    try:
        r, x, y = (float(x) for x in input().split())
        if x == 0:
            slope_of_intersecting_line = None
            slope_of_opposite_line = 0
        elif y == 0:
            slope_of_intersecting_line = 0
            slope_of_opposite_line = None
        else:
            slope_of_intersecting_line = y/x
            slope_of_opposite_line = -1*(x/y)
            

        
        
    except:
        break
