notes = ['A','A#','B', 'C','C#', 'D', 'D#','E','F','F#','G','G#']
scales = []
for i in range(len(notes)):
    scale = [notes[i]]
    j = i
    for p in range(7):
        if p == 0 or p==1 or p==3 or p==4 or p==5:
            j = (j+2) % len(notes)
        else:
            j = (j+1) % len(notes)
        scale.append(notes[j])
    scales.append(scale)

good_scales = {'A': True,
               'A#': True,
               'B': True,
               'C': True,
               'C#': True,
               'D': True,
               'D#': True,
               'E':True,
               'F': True,
               'F#': True,
               'G': True,
               'G#': True}
input()
song = input().split()
for note in song:
    for scale in scales:
        if good_scales[scale[0]] == True and note not in scale:
            good_scales[scale[0]] = False
found_one = False
for key in good_scales.keys():
    if good_scales[key] == True:
        found_one = True
        print(key, end=" ")
if not found_one:
    print("none")

    
    
