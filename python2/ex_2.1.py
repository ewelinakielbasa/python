text = "data to write and read"
file = open('data.txt', 'w')
try:
	file.write(text)
finally:
	file.close()

file = open('data.txt','r')
try:
	text2 = file.read()
finally:
	file.close()

print (text2)