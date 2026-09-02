#wap to take a sentence,detect double spaces and replace them with single spaces
sentence=input("Enter a sentence: ")
doubles=sentence.find("  ")
sentence=sentence.replace("  "," ")
print(sentence)
