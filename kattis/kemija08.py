def decode_sentence(sentence):
    decoded_sentence = ""
    vowels = 'AEIOUaeiou'
    for word in sentence.split():
        i = 0
        while i in range(len(word)):
            if word[i] in vowels:
                decoded_sentence += word[i]
                i += 3
            else:
                decoded_sentence += word[i]
                i += 1

        decoded_sentence += " "

    decoded_sentence = decoded_sentence.strip()
    return decoded_sentence

sentence = input()
print(decode_sentence(sentence))
