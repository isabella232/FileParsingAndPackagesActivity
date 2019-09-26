import re

def calcDistribution(text, word):
    ''' Calculates the percentage of how many times word appears in text
        Percentage = number of times word appears / total amount of words * 100

        Input: "cat cat cat dog", "dog"
        Output: 25 (Since it is 25%)

        Input: "tomato tomatoes tomato", "tomato"
        Output: 66.66
    '''
    textData = wordCounter(text)
    wordFrequencies = textData[0]
    totalWords = textData[1]

    # check if word appears at all
    if word not in wordFrequencies:
        return 0

    return wordFrequencies[word] / totalWords * 100


def wordCounter(text):
    ''' Counts the number of words in text
        Returns a list containing two elements:
            a dictionary of words and their frequencies
            the total amount of words

        Input: "cat cat cat dog"
        Output: [ {("cat" : 3), ("dog" : 1)}, 4 ]
    '''
        
    wordCounts = {}

    # format the raw string into a list of words
    # checks for semicolons, commas, periods, newlines, spaces, ?'s, hyphens to an extent
    wordList = re.split('; *|, *|\. *|\n+| +|\?\ *| *\-+ *', text)

    # using remove() to 
    # perform removal
    while("" in wordList) : 
        wordList.remove("")
    
    # calculate the frequency of each word and total word count
    for word in wordList:
        word.lower()
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1
            
    return [wordCounts, len(wordList)]
