caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
index = {letter: caps.index(letter) for letter in caps}
rev_index = {caps.index(letter): letter for letter in caps}

string = "KOSMMYURUTEMQDMWZILHUSRODY"
phrase = [12, 0, 24, 0]

decoded_string = "".join(rev_index[(index[character]-phrase[i % len(phrase)])%26] for i, character in enumerate(string))

print(decoded_string)
