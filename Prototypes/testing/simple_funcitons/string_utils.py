
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]
