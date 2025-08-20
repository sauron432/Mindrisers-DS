def remove_vowel(user_input:str) -> str:
    vowels = "aeiouAEIOU"
    vowels_removed = ''
    for char in user_input:
        if char not in vowels:
            vowels_removed += char
    return vowels_removed

user_input = input("Enter a string:").strip()
print(remove_vowel(user_input))
