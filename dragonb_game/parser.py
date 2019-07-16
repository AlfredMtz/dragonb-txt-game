# import lexicon


# Parser Error Exception class
class ParserError(Exception):
    pass
# Sentence object
class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]
    
    def __str__(self):
        return f"{self.subject} {self.verb} {self.object}"

#1 What type of word is the first in the list
def peek(word_list):
    if word_list:
        word = word_list[0]
        # Example: noun, verb, etc..
        return word[0]
    else:
        return None
        
#2. I expect the first word in the list to be a 'noun' 'verb' 'etc..'
# if it is return the word tuple, if is not, then return None.
def match(word_list, expecting):
    # for each tuple in list
    if word_list:
        # pop(i) --> remores item at given position in list and returns it
        word = word_list.pop(0)
        # type of word == to expected
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

#3. Skip words that aren't usefull to the sentence
def skip(word_list, word_type):
    # is the first word in the list == word_type
    while peek(word_list) == word_type:
        # If it is, poped it out from the list and check if its == word_type.
        # if it is return the word(won't show thoguh) because there is not a
        # return statement inside of this loop or function, so just keep running
        # the while loop and updating the word_list until it breaks and you
        # finish with an updated list.
        match(word_list, word_type)
    
def parse_verb(word_list):
    # breake the loop and run next block of code once
    # a word in not a 'stop' word
    skip(word_list, 'stop')
    # if the next word in the list is verb
    if peek(word_list) == 'verb':
        # return (type, word)
        return match(word_list, 'verb')
    elif peek(word_list) == 'direction':
        return ('verb', 'go')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if not next_word:
         return ('noun', 'play')
    elif next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    elif next_word == 'direction':
        return('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")
    
def parse_sentence(word_list):
    if word_list[0][0] == 'number':
        return word_list[0][1]
    else:
        subj = parse_subject(word_list)
        verb = parse_verb(word_list)
        obj = parse_object(word_list)

        return Sentence(subj, verb, obj)


# word_list = lexicon.scan("go right")
# print(parse_sentence(word_list))
# print(parse_subject([('verb', 'yes')]))
# print(parse_verb([('verb', 'yes')]))
# print(parse_object([('verb','yes')]))
# print(parse_sentence([('verb', 'yes')]))
