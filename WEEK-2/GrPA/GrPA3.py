str = input().lower()
vowels = ""
if "a" in str:
    vowels = vowels+"a"
if "e" in str:
    vowels = vowels+"e"
if "i" in str:
    vowels = vowels+"i"
if "o" in str:
    vowels = vowels+"o"
if "u" in str:
    vowels = vowels+"u"
if ('a' in vowels or 'e' in vowels or 'i' in vowels or 'o' in vowels or 'u' in vowels):
    
    print(vowels)
else:
    
    print("none")
