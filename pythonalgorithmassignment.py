def hours_to_min(x):
    result = x*60
    return result
print(hours_to_min(3))

def hours_or_min(x):
    choice = input("hours or minutes: ")
    if choice == "hours":
        result = x*60
    elif choice == "minutes": 
        result = x/60
    return result
print(hours_or_min(120))



def wordlen():
    word = input("Enter a word: ")
    letter_count = len(word)
    print(f"The word contains", letter_count, "letters.")

wordlen()