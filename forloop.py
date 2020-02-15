def emoji_converter(message):
    word=message.split(" ")
    dictionary={
	    ":)":"😊",
	    ":(":"😢"
    }
    output=""
    for i in word:
        output+=dictionary.get(i,i)+ " "

    return output
message=input(">")
print(emoji_converter(message))


