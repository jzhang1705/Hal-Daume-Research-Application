#!/usr/bin/python3


# Let n = total number of words in the document 
# Let k = number of distinct words in the document


# Does a binary search to find the insert position of target
# Runtime Complexity: O(1), Memory Complexity: O(1)
# Runtime should be on average log base 2 of 10
def searchInsert(lst, target):
    low = 0
    high = 9
    while low <= high:
        mid = int((low + high)/2)
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low


import sys

# Opens the file in the argument to read
file1 = open(sys.argv[1],"r+") 

# Reads the lines of the file 
Lines = file1.readlines() 
words = {} # Dictionary where key: word, value: number of times the word appears in the file

# Reads line, splits the and turns it into an array of words, updates the "words" dictionary appropriately 
# Runtime Complexity O(n), Memory Complexity: O(k)
for line in Lines:
    line = line.split()
    for word in line:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1 

# Lists to keep track of the top 10 words, set to None and 0 initially
top_ten_words = [None]*10
corresponding_frequencies = [0]*10

# Keeps track of ties for last
tied_for_tenth = []
tenth_place_frequency = 0

# Finds the top 10 words by appending new words and then poping the last word every iteration
# Keeps track of ties if they exit by checking if the popped word frequency is the same as the 10th place frequency word.
# Runtime Complexity: O(k), Memory Compexity: Best Case O(1), Worst Case: O(k)
for word in words:
    insertLocation = searchInsert(corresponding_frequencies, words[word])
    top_ten_words.insert(insertLocation, word)
    corresponding_frequencies.insert(insertLocation, words[word])
    popped_word = top_ten_words.pop(0)
    popped_number = corresponding_frequencies.pop(0)
    if popped_number == corresponding_frequencies[0]:
        tied_for_tenth.append(popped_word)
        tenth_place_frequency = popped_number
    else:
        tied_for_tenth = []
        tenth_place_frequency = 0


# Displays the results based on rank (accounts for tied ranking)
i = 9
rank = 1
previous_frequency = corresponding_frequencies[i]
print(str(rank) + ": " + top_ten_words[i] + " " + str(corresponding_frequencies[i]))

i -= 1
while i >= 0 and corresponding_frequencies[i] != 0:
    if previous_frequency != corresponding_frequencies[i]:
        rank = 10 - i
    previous_frequency = corresponding_frequencies[i]
    print(str(rank) + ": " + top_ten_words[i] + " " + str(corresponding_frequencies[i]))
    i -= 1

i = 0
while i < len(tied_for_tenth) and tenth_place_frequency != 0:
    print(str(rank) + ": " + tied_for_tenth[i] + " " + str(tenth_place_frequency))
    i += 1
