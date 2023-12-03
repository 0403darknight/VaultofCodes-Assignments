from collections import Counter
line_text = "Hello Dark, After all this time always With great power comes great responsibilities All goood things "
freq = Counter(line_text.split()).most_common()
print(freq)