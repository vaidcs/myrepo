
# Given a string, return a new string made of every other
# char starting with the first, so "Hello" yields "Hlo".
# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'

str = input("Enter a string:-")
l = len(str)
def string_bits(str):
    for x in range(0,l,2):
        print(str[x],end="")
    print()
string_bits(str)