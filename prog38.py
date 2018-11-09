# Given a non-empty string like "Code" return a string like
# "CCoCodCode".
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

str = input("Enter a string:-")
l = len(str)
def string_splosion(str):
    for x in range(l):
        for y in range(x+1):
            print(str[y],end="")
    print()

string_splosion(str)