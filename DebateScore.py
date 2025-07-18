#Task: Score a debate between 2 Presidential candidates
#Step 1: Import Libraries

#Step 2: Set up lists and variables (Also need to figure out how to score properly)
i = 1 #Line numbers to help debug reading
wordsForPts = ["we", "the", "people"] #using this list to figure out how points will work
wordsForMorePts = ["united", "states", "america"]
CurrSpeaker = "" #Keep track of current speaker
BidenPts = [] #Keep track of points per line or question (whichever makes more sense)
TrumpPts = [] #Keep track of points per line or question (whichever makes more sense)

#Step 3: Take in debate sample
with open("sample.txt", encoding="utf-8") as transcript:
    for line in transcript:
        
        parts = line.split(":") #Seperate speaker and words
        
#Step 4: Determine who is currently speaking
        if parts[0] == "WALLACE":
            CurrSpeaker = parts[0] 
        if parts[0] == "BIDEN":
            CurrSpeaker = parts[0]
        if parts[0] == "TRUMP":
            CurrSpeaker = parts[0]
        
#Step 5: Determine points
        words = line.split()
        points = 0
        points += sum(1 for word in words if word.lower() in wordsForPts)
        points += sum(2 for word in words if word.lower() in wordsForMorePts)
        
#Step 6: Add points
        if CurrSpeaker == "BIDEN":
            BidenPts.append(points)
        if CurrSpeaker == "TRUMP":
            TrumpPts.append(points)
        else: points = 0

#Step 7: Total them up
TrumpTotal = sum(TrumpPts)
BidenTotal = sum(BidenPts)
print(f"Trumps Points: {TrumpTotal}, Bidens Points: {BidenTotal}") #Output for testing
if TrumpTotal > BidenTotal:
    print("Winner: Trump")
if TrumpTotal < BidenTotal:
    print("Winner: Biden")
else:
    "Unable to determine"