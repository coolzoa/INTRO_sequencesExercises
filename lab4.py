"""
Author: Jose Pablo Murillo
File: lab4
Description: Use of for and while
Last update: 20/06/2019
Python version 3.7
"""

#Exercise 1
def removeElement(element, collection: list) -> list:
    """
    Input: A list and an element of any type
    Output: The collection without the element or error
    Process: We iterate through each index to see if the current matches
        the element, if it does it will not be added to the result
    Restrictions: Collection must be type list
    """
    if (not isinstance(collection, list)):
        return "Error, collection must be list"
    else:
        result = list()
        for currentElement in collection:
            if (currentElement != element):
                result = result + [currentElement]
        return result

#Exercise 2
def listIndexes(element, collection: list) -> list:
    """
    Input: A list and an element of any type
    Output: A list with indexes of where element appears (first index is 0)
        or error
    Process: We iterate through each index to see if the current matches
        the element, if it does it will be added to the result
    Restrictions: Collection must be type list
    """
    if (not isinstance(collection, list)):
        return "Error, collection must be list"
    else:
        indexes = list()
        length = len(collection)
        for i in range(0, length):
            if (collection[i] == element):
                indexes = indexes + [i]
        return indexes

#Exercise 3
def positiveNegative(collection: list) -> list:
    """
    Input: A list
    Output: A list with two sublists containing positive and negative numbers
        found or erro
    Process: We iterate through each index to see if the current matches
        the element, if it does it will be added to the result
    Restrictions: Collection must be type list
    """
    if (not isinstance(collection, list)):
        return "Error, collection must be list"
    
    positives = list()
    negatives = list()
    length = len(collection)
    for i in range(0, length):
        if (type(collection[i]) == int):
            if (collection[i] < 0):
                negatives = negatives + [collection[i]]
            else:
                positives = positives + [collection[i]]
    return [positives, negatives]

#Exercise 4
def province(province: int, Ids: list) -> list:
    """
    Input: A number of province
    Output: A list of ids whose leftmost digit is equal to the province
    Process: We iterate through each index and check the leftmost digit with
        the province, we get is with the help of numberLength
    Restrictions: Collection must be type list, province must be int between
        1 and 7
    """
    if (not isinstance(province, int)):
        return "Error, province must be integer"
    elif (province < 0):
        return "Error, province must be positive"
    else:
        if (province not in range(1, 8)):
            return "Errror, province must be between 1 and 7"
        else:
            matches = list()
            for currentId in Ids:
                if (type(currentId) == int):
                    if (currentId > 0):
                        length = numberLength(currentId)
                        currentProvince = currentId // 10**(length - 1)
                        if (currentProvince == province):
                            matches = matches + [currentId]
            return matches
                        

def numberLength(number: int) -> int:
    if (number == 0):
        return 1
    else:
        count = 0
        while (number != 0):
            number = number // 10
            count = count + 1
        return count

#Exercise 5
def createList(numberElements: int) -> list:
    """
    Input: A number indicating number of elements of the list
    Output: A list full of 0s or error each 0
    Process: while we still have to produce, we generate a 0
        and subtract 1 from numberElements
    Restrictions: numberElements must be int
    """
    if (not isinstance(numberElements, int)):
        return "Error, number must be integer"
    else:
        result = list()
        while (numberElements > 0):
            result = result + [0]
            numberElements = numberElements - 1
        return result

def registerTime(runner: int, time: float, collection: list) -> list:
    """
    Input: A runner number, the time it took to reach a goal mm,ss and
        the collection to add to
    Output: A list with the registered runner and time or error
    Process: We first see if the index is reachable, then insert in the position
    Restrictions: Runner must be positive integer, time must be positive float,
        collection must be type list
    """
    if (not isinstance(collection, list)):
        return "Error, collection must be list"

    if (not isinstance(time, float)):
        return "Error, time must be float"
    elif (time < 0):
        return "Error, time must be positive float"

    if (not isinstance(runner, int)):
        return "Error, runner number must be integer"
    elif (runner <= 0):
        return "Error, runner number must be greater than 0"
    else:
        length = len(collection)
        if (runner - 1 in range(length)):
            collection[runner - 1] = time
        else:
            return "Error, runner has no place in the collection"

def findWinner(runnerTimes: list) -> float:
    """
    Input: A list of runner times
    Output: The winner with the least time or error
    Process: We iterate through the least and keep the lowest time in current
    Restrictions: runnerTimes must be list and have at least one time
    """
    if (not isinstance(runnerTimes, list)):
        return "Error, runner times must be a list"
    else:
        if (len(runnerTimes) < 1):
            return "Error, no times are registered"
        else:
            winnerTime = runnerTimes[0]
            winnerId = 1
    
            runnerTimes = runnerTimes[1:]
            currentRunnerId = 2
            
            for time in runnerTimes:
                if (time < winnerTime and time > 0):
                    winnerTime = time
                    winnerId = currentRunnerId
                else:
                    currentRunnerId = currentRunnerId + 1
            return [winnerId, winnerTime]



#Exercise 6
def fib(n: int) -> tuple:
    """
    Input: number of terms that want to be presented from fibonacci sequence
    Output: The first n terms of Fibonacci sequence or error
    Process: We calculate the first two terms and the next is the sum
        of the previous two so we continue doing this until n == 0
    Restriccionts: n must be int and >= 1
    """
    if (not isinstance(n, int)):
        return "Error, input must be integer"

    if (n <= 0):
        return "Error, input must be integer greater than or equal to 1"

    first = 0
    step = 1
    result = tuple()
    result = result + (first, step,)
    if (n == 1):
        return result[0:1]
    elif (n == 2):
        return result
    
    while (n > 2):
        temp = first + step
        result = result + (temp,)
        first = step
        step = temp
        n = n - 1
    return result




#Exercise 7
def indexFib(m: int) -> int:
    """
    Input: the m-th term of the fibonacci sequence
    Output: the corresponding term in the sequence
    Process: We use fib to get the tuple and then index it taking 1 as
        first index
    Restrictions: m must be integer >= 1
    """
    if (not isinstance(m, int)):
        return "Error, input must be integer"
    if (m < 1):
        return "Error, input must be integer greater than or equal to 1"
    result = fib(m)
    m = m - 1
    return result[m]



#Exercise 8
def eliminateSpaces(inp: str) -> (str, int):
    """
    Input: a string
    Output: the string without spaces and the number of spaces deleted
    Process: we iterate through each index and check if it is a space,
        if it is we increase the counter of spaces and delete it from result
    Restrictions: input must be string
    """
    if (not isinstance(inp, str)):
        return "Error, input must be string"
    countSpaces = 0
    result = str()
    for element in inp:
        if (element == " "):
            countSpaces = countSpaces + 1
        else:
            result = result + element
    return result,countSpaces



#Exercise 9
def countWords() -> None:
    """
    Inputs: nothing
    Outputs: none
    Process: we ask for the number of words that want to be counted
        We setup the tuple with words and make sure it doesn't have repeated
        we then call the function that registers phrases passing the words
        as parameter. The function then prints the counts of each word found
        for the input phrases
    Restrictions: function must be called with no parameters
    """
    inp = input("How many words would you like to register? :")
    words = tuple()
    try:
        n = int(inp)
        while (n > 0):
            word = input("Type the word: ")
            word,count = eliminateSpaces(word)
            if (word not in words):
                words = words + (word,)
            n = n - 1
        print("Tuple of words: " + str(words))
        askPhrases(words)
                
    except ValueError:
        print("You must enter a number")
        countWords()

def askPhrases(words: tuple) -> None:
    inp = input("How many phrases would like to register? :")
    amountWords = len(words)
    counts = createList(amountWords)
    try:
        n = int(inp)
        while (n > 0):
            phrase = input("Type the phrase: ")
            phraseSplit = phrase.split(" ")
            for i in phraseSplit:
                if (i in words):
                    index = words.index(i)
                    counts[index] = counts[index] + 1
            n = n - 1
        print("Amount of times that appears each word in the phrases")
        for word in words:
            index = words.index(word)
            print(word + ": " + str(counts[index]))
    except ValueError:
        print("You must enter a number")
        askPhrases(words)



#Exercise 10
def isPalindrome(entry: str) -> bool:
    """
    Inputs: string
    Outputs: boolean that says if string is palindrome, meaning it is
        read the same left->right and right<-left
    Process: We get indexes of the beginning and end of the string
        Then we check if they are equal and then move forward and backward
        until we reach when indexes are pointing at same element.
    Restrictions: input must be string
    """
    
    length = len(entry)
    if (length == 0):
        return False
    elif (length == 1):
        return True
    else:
        maxIndex = length - 1
        minIndex = 0
        
        while (minIndex < maxIndex):
            if (entry[minIndex] != entry[maxIndex]):
                return False
            else:
                minIndex += 1
                maxIndex -= 1
        return True




#Exercise 11
def getDigitsFromString(entry: str) -> str:
    """
    Inputs: input data
    Outputs: string containing found digits or null
    Process: We iterate through the string and check if char can be
        converted to number
    Restrictions: None
    """

    result = str()
    for i in entry:
        try:
            int(i)
            result = result + i
            
        except ValueError:
            pass
    return result



#Exercise 12
def numDigits(entry: str) -> int:
    """
    Inputs: input data
    Outputs: Amount of digits in data
    Process: We filter the string to reduce it to only digits, then we
        calculate its length
    Restrictions: None
    """

    digitsString = getDigitsFromString(entry)
    return len(digitsString)



#Exercise 13
def symmetricDifference(entry1: str, entry2: str) -> str:
    """
    Inputs: First string and second string
    Outputs: Symmetric difference: elements that exist in one string
        or the other but not both
    Process: We iterate for each string and check if it is in
        the other string or in the shared pool
    Restrictions: function must be called with no parameters
    """
    difference = str()
    shared = str()
    for i in entry1:
        if (i not in entry2):
            if (i not in shared):
                difference += i
                shared += i

    for i in entry2:
        if (i not in entry1):
            if (i not in shared):
                difference += i
                shared += i

    return difference   

        
        
                    
                    
                    
                
            
    
            
