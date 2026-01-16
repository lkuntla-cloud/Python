ABC=(input("Enter a character: "))
if len(ABC)>1:
    print("Enter only one character")

if ('a'<=ABC<='z')or('A'<=ABC<='z'):
    print("Your character is in the alphabet")
else:
    print("Your character is not in the alphabet")