# emoji converter
message = input(">")
words = message.split(" ")
emojies = {
    ":)": "🙂",
    ":(": "😔",
    "fish": "🐟",

}
output = ""
for word in words:
    output = output + emojies.get(word, word) + " "
print(output)

# emoji coverter function

def emoji_converter(message):
    words = message.split(" ")
    emojies = {

    ":)": "🙂",
    ":(": "😔",
    "fish": "🐟",

    }
    output = ""
    for word in words:
        output = output + emojies.get(word, word) + " "
    return output

try:
    message = input(">")
    print(emoji_converter(message))
except ValueError:
    print("Error")
