'''
wap to input a std's marks in n consecutive tests and store them in a list.Find the longest consecutive sequence in which each mark is strictly greater than the previous mark.
Display the sequence,its length,and its staeting and ending tesgt numbers as a tuple.If multiple sequence have the same maximum length, display the first one.
MArks:[55,60,68,62,65,70,78,74]
Longest improving sequence:[62,65,70,78]
no. of tests:4
test range:(4,7)
conditions:
accept at lest one test
Equal marks break the improving sequence
Test numbers begin at 1
do not sort the list because the original order matters.
'''
marks = []

n = int(input("Enter number of tests: "))

for i in range(n):
    marks.append(int(input("Enter marks: ")))

best = []
current = [marks[0]]

start = 1
best_start = 1

for i in range(1, n):
    if marks[i] > marks[i - 1]:
        current.append(marks[i])
    else:
        if len(current) > len(best):
            best = current
            best_start = start

        current = [marks[i]]
        start = i + 1

if len(current) > len(best):
    best = current
    best_start = start

best_end = best_start + len(best) - 1

print("Longest improving sequence:", best)
print("No. of tests:", len(best))
print("Test range:", (best_start, best_end))
