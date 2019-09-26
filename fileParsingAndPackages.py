import word_distribution_calculator_modified as WDCM

def countWords(speeches, word):
    ''' passes in arguments to another function '''
    for title in speeches:
        distr = WDCM.calcDistribution(speeches[title], word)
        print(distr)

        
def read(filename, delimiter):
    ''' opens filename and parses it line by line using delimiter
        to determine the start of a new speech
    '''
    speeches = {}
    
    with open(filename, 'r') as file:
        # remove newlines
        fileData = file.read().split('\n')
        
        prevLine = fileData[0]
        for line in fileData[1:]:
            if (prevLine == delimiter):
                title = line
            else:
                if title not in speeches:
                    speeches[title] = line
                else:
                    speeches[title].join(" " + line + " ")
            prevLine = line
    print(speeches[title])
    return speeches


def main():
    speeches = read("speechSnippets.txt", "-----")
    countWords(speeches, "the")
    
