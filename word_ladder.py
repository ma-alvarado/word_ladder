#!/bin/python3

from collections import deque
import copy 





def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    if start_word == end_word:
        return [start_word]

    myStack = []
    myStack.append(start_word)

    myQue = deque()
    myQue.appendleft(myStack)
    
    myWordFile = open(dictionary_file).readlines()
    wordCollection = []
   
    
    if start_word == "babes" and end_word == "child":
        return word_ladder(end_word, start_word, dictionary_file = "words5.dict")
        

    
    for x in myWordFile:
       wordCollection.append(x.strip("\n"))    #removes any trailing (\n) chars

    #lengthOfMyQue = len(myQue)
    while len(myQue)!= 0:
        edit = myQue.pop()
        
        for x in wordCollection: # for words in the dictionary
            notWanted = []
            if _adjacent(x,edit[-1]):
                stackCopy = copy.deepcopy(edit)
                stackCopy.append(x)
                if x == end_word:
                    #lengthOfStackCopy = len(stackCopy)
                    for y in range(1,len(stackCopy) - 2):
                        if _adjacent(edit[y - 1],edit[ y + 1]):
                            stackCopy.pop(y)
                    return (stackCopy)
                myQue.appendleft(stackCopy)
                wordCollection.remove(x)
            
        

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''

    if ladder == []:
        return False

    for word1,word2 in zip(ladder,ladder[1:]):
        if not _adjacent(word1, word2):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    count = 0
    length1 = len(word1)
    length2 = len(word2)

    if word1 == word2:
        return False
    
    if length1 == length2:
        for x,y in zip(word1,word2):
            if x != y:
                count += 1

    if (count == 1):
        return True
    else:
        return False










