# Complete the findNumber function below.
def SpellingBeeSolutions(wordlist, puzzles):
    word_check = []
    for word in wordlist:
        for l in word:
            word_letter = l
            for word_puzzle in puzzles:
                print(word_puzzle)
                if word_letter in word_puzzle:
                    print(word_letter)
                else:
                    pass
   
    # for puzzle in puzzles:
    #     for l in puzzle:
    #         if l in wordlist:
    #             word = word.append(l)
    # print(word)

    # for word in wordlist:
    #     print(word)






wordlist = ['APPLE', 'PLEAS', 'PLEASE']
puzzles = ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPXY', 'XAELPSY']
SpellingBeeSolutions(wordlist, puzzles)
