user_input = input("Enter a string:").strip().lower()
count = 0
space = 0
vowels = "aeiou"

for c in user_input:
    if c in vowels:
        count += 1
    elif c == ' ':
        space +=1

print("Number of vowels:",count)
print("Number of consonants:",len(user_input)-count-space)
        

    
    