def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

string = input("Enter a string: ")

if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")