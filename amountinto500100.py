#Enter an amount and how many 500 and 100 notes are required
money=int(input(" "))
notes_500=money//500
notes_100=money% 500
print(f"{money}= {notes_500} notes of 500 and {notes_100} notes of 100")