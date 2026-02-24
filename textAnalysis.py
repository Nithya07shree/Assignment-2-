"""
TEXT ANALYSIS (Question 19)
INPUT: input text
OUTPUT: number of words, vowels, consonants, reversed text, palindrome check, removed vowels, word frequency, longest word
"""
# number of words
def numWords(text):
    return len(text.split())

# number of vowels and consonants
def numVowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for i in text: 
        if i in vowels:
            count+=1
    return count

# consonants
def numCons(text):
    vowels = "aeiouAEIOU"
    count =0
    for i in text:
        if i.isalpha() and i not in vowels:
            count+=1
    return count


# reverse text
def reverseText(text):
    return text[::-1]

# palindrome
def isPalindrome(text):
    text2 = text.replace(" ","").lower()
    if text2 == text2[::-1]:
        return "Yes"
    else:
        return "No"

# remove vowels
def removeVowels(text):
    vowels = "aeiouAEIOU"
    res = ""
    for i in text:
        if i not in vowels:
            res+=i
    return res

# Longest word
def longestWord(text):
    words = text.split()
    res=""
    for word in words:
        if len(word)>len(res):
            res=word
    return res

# Word frequency (used dictionary coz it was mentioned in the question)
def wordFreq(text):
    words = text.lower().split()
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq

def analyzeText(text):
    print("======TEXT ANALYSIS======")
    print(f"Words: {numWords(text)}")
    print(f"Vowels: {numVowels(text)}")
    print(f"Consonants: {numCons(text)}")
    print(f"Reversed text: {reverseText(text)}")
    print(f"Palindrome: {isPalindrome(text)}")
    print(f"Without vowels: {removeVowels(text)}")
    print(f"Longest word: {longestWord(text)}")
    freq= wordFreq(text)
    print(f"Word frequency: ",end=" ")
    for key,val in freq.items():
        print(f"{key}: {val}",end=", ")
    print()

text = input("Enter text: ")
analyzeText(text)