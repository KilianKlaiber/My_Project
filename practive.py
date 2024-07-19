
dictionary = {
    "birthday": 8,
    "meeting": {},
    "events": {},
    "date": "ein datum"
    
}

dictionary["birthday"] = {"Ole": 20,
                          "kilian": 40}

print(dictionary)




# Write to dictionary
dictionary["birthday"]["kilian"] = 50

# Read from dictionary
datum = dictionary["birthday"]["Ole"]

print(datum)



