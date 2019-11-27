def get_counts(file_name):     

    dictionary = dict() #Empty dictionary
    
    file = open(file_name,'r') #Open files and put it in read mode
    
    count = 0 #The count variable, used to count how many words there are
    
    for line in file: 
        text = file.read() #This takes the whole text itself
        raw_words = text.split() #This splits it into words
        
        for i in range(0, len(raw_words)): #Looping from 0 to 
            words = raw_words[i].lower()
            if words in dictionary: #If the words are already in the dictionary, I added one to it
                dictionary[words] = dictionary[words] + 1
                count = count + 1 
            else:
                dictionary[words] = 1 #If the words are not in the dictionary, I make a new element and make it equal to one.
                count = count + 1 
        

    dictionary.update({'_total': count}) #Adds the last element "Total" into the dictionary with the amount of words
    
    print (dictionary) #Prints out the dictionary, to see how frequently used each words are
    
    file.close() #Closes file

get_counts("hamlet-short.txt") 

            
        






    









