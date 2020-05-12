import keyword
keys=["for","while","if","break","sky","test"]
for i in range(len(keys)):
    if keyword.iskeyword(keys[i]):
        print(keys[i] + " is python keyword ")
    else:
        print (keys[i] + " is not python keyword")
            
