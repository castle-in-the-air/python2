message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😃",
    ":(": "☹️",
    "angle": "😇",
    "lol": "😜",
    "angry": "😡"
}
output = ""
for word in words:
    output += emojis.get(word, word)+" "
print(output)