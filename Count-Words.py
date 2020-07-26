text="Hello! This is a sample text."
wnum = 1
cnum = 0
for i in text:
    cnum +=1
    if (i == " "): # function counting words depending on number of spaces
        wnum += 1
print("Number of words in sample text were: ", wnum)
print ("Number of characters in sample text were: ",cnum)     # Can be done using: print(f"Number of Characters in sample text were : {len(text)}")
