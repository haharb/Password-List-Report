#Name: Hassan Harb
#Purpose: This program generates a small report regarding a list of approximately a million commonly used passwords. 

# Returns a dictionary of character occurences.
def returnCharacterOccurences(list):
    dictionary = {}
    for line in list:
        for char in line:
            if char != "\n":
                if char in dictionary:
                    dictionary[char] += 1
                else:
                    dictionary[char] = 1
    return dictionary

file = open("pass.txt", "r")
data = file.readlines()
dict = returnCharacterOccurences(data)
lChar = min(dict, key = dict.get)
mChar = max(dict, key = dict.get)
dataLength = len(data)
minimum = min(data, key = len)[:-1]
maximum = max(data, key = len)[:-1]
average = sum([len(string[:-1]) for string in data])/dataLength
print("The list contains " + str(dataLength) +" passwords")
print("The shortest password is: " + minimum + " and the longest password is: " + maximum)
print("The length of the passwords in the list range from " + str(len(minimum)) + " to "+ str(len(maximum)))
print("The average length of the passwords is around " + str(round(average)))

print("The most commonly used character in the list is: " + mChar + " and the least commonly used is: " + lChar + "\n\n")
print("This is the dictionary of characters with their frequencies for further review: " + str(dict))