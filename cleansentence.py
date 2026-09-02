#wap to take a sentence containing double spaces and unwanted spaces at the begining or end.Clean the sentence
s=input("Enter a sentence: ")
s=s.strip()
s=s.replace("  "," ")
print(s)
