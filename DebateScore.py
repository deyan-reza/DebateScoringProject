#Task: Score a debate between 2 Presidential candidates
#Step 1: Import Libraries
#Step 2: Take in debate sample
i = 1
with open("sample.txt") as transcript:
    for line in transcript:
        print(i,line)
        i = i+1