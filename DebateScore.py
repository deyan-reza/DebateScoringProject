#Task: Score a debate between 2 Presidential candidates
#Step 1: Import Libraries
#Step 2: Set up lists and variables
i = 1 #Line numbers to help debug reading
wordsForPts = ["we", "the", "people"] #using this list to figure out how points will work
CurrSpeaker = "" #Keep track of current speaker
BidenPts = [] #Keep track of points per line or question (whichever makes more sense)
TrumpPts = [] #Keep track of points per line or question (whichever makes more sense)
#Step 3: Take in debate sample
with open("sample.txt", encoding="utf-8") as transcript:
    for line in transcript:
        
        parts = line.split(":") #Seperate speaker and words
        
        #Determine who is currently speaking
        if parts[0] == "WALLACE":
            CurrSpeaker = parts[0] 
        if parts[0] == "BIDEN":
            CurrSpeaker = parts[0]
        if parts[0] == "TRUMP":
            CurrSpeaker = parts[0]
        
        #Determine points
        words = line.split()
        points = 0
        points += sum(1 for word in words if word.lower() in wordsForPts)
        
        #Add points
        if CurrSpeaker == "BIDEN":
            BidenPts.append(points)
        if CurrSpeaker == "TRUMP":
            TrumpPts.append(points)
        else: points = 0
            
print(f"TrumpPts: {sum(TrumpPts)}, BidenPts: {sum(BidenPts)}")  #Output for testing