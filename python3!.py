
def countWords():
    filename=input('Enter the filename')
    file= open(filename,'r')
    totalWords= 0
    for line in file:
        words=line.split()
        totalWords=totalWords+len(words)
    print(totalWords) 
countWords()

    
    
