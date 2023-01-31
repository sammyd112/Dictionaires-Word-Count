"""Count words in file."""

# import test.txt


def count_words(text):
    counts = {}
    text = open(text)
    for line in text:
        line = line.split()
        for word in line:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    for key, count in counts.items():
        print(key, count)

count_words('test.txt')
# put your code here.
