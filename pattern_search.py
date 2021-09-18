from words import string_list 
from os import system
import time
def naive_pattern_search(text, pattern):

    num_skips = 0
    for text_idx in range(len(text)):
        match_count = 0 
        if num_skips > 0:
            num_skips -= 1
            continue 
        else:
            for pattern_idx in range(len(pattern)):
                try:
                    if pattern[pattern_idx] == text[pattern_idx + text_idx]:
                        match_count += 1
                    else:
                        break 
                except IndexError:
                    break
            
        
        if len(pattern) == match_count:
            print("Pattern found at Index: {}".format(text_idx))
            return 'profanity found'
            num_skips = len(pattern) - 1
    
    return True


def filter():
    text = str(input(': '))
    for word in string_list:
        text = text.lower()
        text = text.strip()
        word = word.lower()
        checker = naive_pattern_search(text, word)
        phrase_checker = 'You are '
        if phrase_checker in text:
            time.sleep(0.5)
            print("Profanity found")
            return
        elif checker == True:
            continue 
        else:
            return checker 
    
    return 'No Profanity Found'


print(filter())