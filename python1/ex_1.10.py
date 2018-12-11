with open('example_text.txt') as f:
    words = f.read().split()

newWords=[]

for word in words:
    if word == "i":
        word = "oraz"
    elif word== "oraz":
        word = "i"
    elif word== "nigdy":
        word = "prawie nigdy"
    elif word== "dlaczego":
        word = "czemu"

    newWords.append(word)
print(words)
print(newWords)
