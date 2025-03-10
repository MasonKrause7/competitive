alternates = {'A#':'Bb',
              'Bb':'A#',
              'C#':'Db',
              'Db':'C#',
              'D#':'Eb',
              'Eb':'D#',
              'F#':'Gb',
              'Gb':'F#',
              'G#':'Ab',
              'Ab':'G#'}
case_num = 1
while True:
    try:
        note,tonality = input().split()
        if note in alternates:
            print(f"Case {case_num}: {alternates[note]} {tonality}")
        else:
            print(f"Case {case_num}: UNIQUE")
        case_num += 1
    except:
        break

