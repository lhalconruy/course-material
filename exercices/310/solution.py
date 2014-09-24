f = open('word')
text = f.read().replace('\n', '')
print(text.count('e'))
