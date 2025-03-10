n = int(input())
notes = input().split()


staff = {'G': '',
         'F': '',
         'E': '',
         'D': '',
         'C': '',
         'B': '',
         'A': '',
         'g': '',
         'f': '',
         'e': '',
         'd': '',
         'c': '',
         'b': '',
         'a': ''}

for note in notes:
    if len(note) == 1:
        staff[note]+= "*"
        for key in staff.keys():
            if key != note:
                if key in "GECAfdcb":
                    staff[key]+=" "
                else:
                    staff[key]+="-"
        for key in staff.keys():
            if key in "GECAfdcb":
                staff[key]+=" "
            else:
                staff[key]+="-"
    elif len(note) > 1:
        multiplier = int(note[1])
        for i in range(multiplier):
            staff[note[0]] += "*"
            for key in staff.keys():
                if key != note[0]:
                    if key in "GECAfdcb":
                        staff[key]+=" "
                    else:
                        staff[key]+="-"
        for key in staff.keys():
                if key in "GECAfdcb":
                    staff[key]+=" "
                else:
                    staff[key]+="-"

for key in staff.keys():
    print(f"{key}: {staff[key][:-1]}")
