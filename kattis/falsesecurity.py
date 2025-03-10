letters_to_morris = {'A': '.-', 'B':'-...', 'C': '-.-.', 'D': '-..', 'E':'.',
                     'F': '..-.', 'G': '--.', 'H':'....','I':'..','J':'.---',
                     'K':'-.-', 'L': '.-..', 'M':'--', 'N': '-.', 'O': '---',
                     'P': '.--.', 'Q':'--.-', 'R':'.-.', 'S': '...', 'T':'-',
                     'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
                     'Z': '--..', '_':'..--', '.':'---.', ',':'.-.-', '?':'----'}

morris_to_letters = {letters_to_morris["A"]: "A",
                     letters_to_morris["B"]: "B",
                     letters_to_morris["C"]: "C",
                     letters_to_morris["D"]: "D",
                     letters_to_morris["E"]: "E",
                     letters_to_morris["F"]: "F",
                     letters_to_morris["G"]: "G",
                     letters_to_morris["H"]: "H",
                     letters_to_morris["I"]: "I",
                     letters_to_morris["J"]: "J",
                     letters_to_morris["K"]: "K",
                     letters_to_morris["L"]: "L",
                     letters_to_morris["M"]: "M",
                     letters_to_morris["N"]: "N",
                     letters_to_morris["O"]: "O",
                     letters_to_morris["P"]: "P",
                     letters_to_morris["Q"]: "Q",
                     letters_to_morris["R"]: "R",
                     letters_to_morris["S"]: "S",
                     letters_to_morris["T"]: "T",
                     letters_to_morris["U"]: "U",
                     letters_to_morris["V"]: "V",
                     letters_to_morris["W"]: "W",
                     letters_to_morris["X"]: "X",
                     letters_to_morris["Y"]: "Y",
                     letters_to_morris["Z"]: "Z",
                     letters_to_morris["_"]: "_",
                     letters_to_morris["."]: ".",
                     letters_to_morris[","]: ",",
                     letters_to_morris["?"]: "?"
                     }

while True:
    try:
        message = input()
    except:
        break
    morris = ""
    lengths = []
    for char in message:
        morris += letters_to_morris[char]
        lengths.append(len(letters_to_morris[char]))
    list.reverse(lengths)

    index = 0
    untangled = ""
    for length in lengths:
        curr_morris = ""
        for i in range(length):
            curr_morris += morris[index]
            index += 1
        untangled += morris_to_letters[curr_morris]
    print(untangled)
    
