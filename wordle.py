import string
import requests
import time
from itertools import product

def generateCombos(missingLetters: int, availableLetters: list[str]=string.ascii_lowercase) -> list[list[str]]:
    return list(product(availableLetters, repeat=missingLetters))

def main():
    availableLetters = list(input("What letters are available?: "))
    missingLetters = int(input("How many letters are left?: "))
    confirmedSoFar = list(input("What greens do you have (enter ' ' for slots that aren't confirmed green)?: "))
    combos = generateCombos(missingLetters, availableLetters)

    possibleGuesses = []
    for combo in combos:
        # print(combo)
        guess = confirmedSoFar[ : ]
        comboIdx = 0
        guessIdx = 0
        while guessIdx < len(guess):
            if guess[guessIdx] == ' ':
                # print(combo[comboIdx])
                guess[guessIdx] = combo[comboIdx]
                comboIdx += 1
            guessIdx += 1
        possibleGuesses.append(guess)
    
    print("\n**** POSSIBLE WORDS ****")
    for guess in possibleGuesses:
        word = "".join(guess)
        #url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        #print(url)
        time.sleep(0.05)    # just to avoid getting blocked by sending too many requests at once
        r = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if r.status_code == 200:
            print(word)
    print("**** END POSSIBLE WORDS ****")

if __name__ == "__main__":
    main()
