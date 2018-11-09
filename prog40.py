
# Given a string and a non-negative int n, we'll say that the
# front of the string is the first 3 chars, or whatever is there if the
# string is less than length 3. Return n copies of the front.
# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'

str = input("Enter a String:-")
n = int(input("How Many Front Copies you Want:-"))
if len(str)>2:
    l = 3
else:
    l = len(str)

def front_times(str,n):
    for x in range(n):
        for y in range(l):
            print(str[y],end="")
    print()

front_times(str,n)