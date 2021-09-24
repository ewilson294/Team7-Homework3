""" 
Homework 3
Problem 1
Team#: 7
Team Member-1: Eric Wilson - Member’s Contribution 33%
Team Member-2: Ha Tran - Member’s Contribution 33%
Team Member-3: Quynh Tran - Member’s Contribution 33%
"""
#Use a while loop to allow user to run repeat the calculation
again = 'y'
while again.lower() == 'y':
    #Prompt the user to enter a tweeter string
    tweet = input('Enter a tweet: ')

    #Count the number of words
    spacecount = 0
    for letter in tweet:
        if letter == ' ':
            spacecount += 1
        wordcount = spacecount + 1
    print("Number of words", wordcount)

    #Calculate the average number of characters in each word
    print("Average number of characters: ", round((len(tweet) - spacecount)/wordcount,2))

    #P1.3 - Count upper case letters
    count = 0
    for letter in tweet:
        if letter.isupper() :
            count += 1
    print("Number of upper case leteers: ", count)

    #P1.4 - Count lower case letters
    count = 0
    for letter in tweet:
        if letter.islower() :
            count += 1
    print("Number of lower case leteers: ", count)

    #P1.5 - Reverse the string
    count = len(tweet)
    rev = ""
    while count >0 :
        count = count - 1
        rev += tweet[count]
    print("Your tweet reversed:" ,rev)

    def cal_str_stats(mystr):
        count = 0
        for letter in mystr:
            if letter.isalpha():
                count += 1
        print("Number of alphabets (a to z, and A to Z): ", count)
    
        count = 0
        for letter in mystr:
            if letter.isdigit():
                count += 1
        print("Number of digits 0 to 9: ", count)
    
        count = 0
        for letter in mystr:
            if not(letter.isdigit() or letter.isspace() or letter.isalpha()):
                count += 1
        print("Number of special characters (such as #, $, @): ", count)
    
    #call the function to calculate string stats
    cal_str_stats(tweet)
    
    #Ask the user to repeat or stop
    again = input('Do you want to analyze another data? Enter "y" to repeat. Enter anything else to stop. ')
