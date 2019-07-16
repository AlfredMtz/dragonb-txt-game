'''
The scan() fucntion should take a string sentence,
break it down into words and return a list of tuples
which include the ('wordtype', 'word')
'''

lexicon_dict = {
    'down': 'direction',
    'up': 'direction',
    'left': 'direction',
    'right': 'direction',
    'back': 'direction',
    'north': 'direction',
    'south': 'direction',
    'west': 'direction',
    'east': 'direction',
    'turn': 'verb',
    'next': 'verb',
    'go': 'verb',
    'run': 'verb',
    'stop': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'fight': 'verb',
    'shoot': 'verb',
    'dodge': 'verb',
    'tell': 'verb',
    'throw': 'verb',
    'slowly': 'verb',
    'yes': 'verb',
    'no': 'verb',
    'raise': 'verb',
    'place': 'stop',
    'a': 'stop',
    'the': 'stop',
    'to': 'stop',
    'in': 'stop',
    'of': 'stop',
    'from': 'stop',
    'at': 'stop',
    'it': 'stop',
    'bomb': 'noun',
    'joke': 'noun',
    'door': 'noun',
    'bomb': 'noun',
    'gothons': 'noun',
    'dragon': 'noun',
    'eternal': 'noun',
    'them': 'noun'
}

def scan(words):
    # Change to lower case
    words = words.lower()
    # Splits sentence into list of words
    splitted_words = words.split()
    
    pairs_list = []
    # for each word in the list of words.
    for word in splitted_words:
        # if word is in the lexicon_diccionary keys
        if word in lexicon_dict.keys():
            pairs = ((lexicon_dict.get(word), word))
            pairs_list.append(pairs)
    
        # else if the word is not in the diccionary keys
        elif word not in lexicon_dict.keys():
            # Try to make a number
            num = convert_number(word)
            # If not a number
            if num == None:
                pairs = ('error', word)
                pairs_list.append(pairs)
            # If a number
            else:
                pairs = (('number', num))
                pairs_list.append(pairs)
        # Otherwise is an error
        else:
            pass

    #print(pairs_list)
    return pairs_list

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

#scan('123 south east asldfjsdlf')      
