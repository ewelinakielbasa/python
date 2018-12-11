with open('example_text.txt') as f:
    words = f.read().split()

wordsToRemove = ['sie', 'i', 'oraz', 'nigdy','dlaczego']
print(words)
for word in words:
    if word in wordsToRemove:
        words.remove(word)

print(words)