# The goal of this exercise is to convert a string to a new string where each 
# character in the new string is "(" if that character appears only once in the 
# original string, or ")" if that character appears more than once in the original
# string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

def solution(word): # O(n**2)
    result_string = '' # O(1)
    for letter in word.lower(): # O(n)
        if word.count(letter) == 1: # O(n)
            result_string += '('
        else:
            result_string += ')'
    return result_string


def solution(string):
    char_count = {}
    string = string.lower()
    for letter in string:
        char_count[letter] = char_count.get(letter, 0) + 1
    new_string = ''
    for letter in string:
        new_string += '(' if char_count[letter] == 1 else ')'
    return new_string
