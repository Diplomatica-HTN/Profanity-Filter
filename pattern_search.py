from words import string_list 
from os import system
import time
from script import backend
import names
import random 

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
                return 'profanity found'
                num_skips = len(pattern) - 1
    
    return True

def filter():
    text = str(input(': '))
    if text == '/end':
        return
    for word in string_list:
        text = text.lower()
        text = text.strip()
        word = word.lower()
        checker = naive_pattern_search(text, word)
        phrase_checker = 'You are '
        if phrase_checker in text:
            time.sleep(0.5)
            print("Profanity found. You are restricted to sending this message.")
            return
        elif checker == True:
            continue 
        else:
            return checker 
    print('No Profanity Found')
    return text

def beta_convo():
    user_2 = names.get_full_name()
    user_1 = names.get_full_name()
    conversation = []
    
    
    while True:
        result_text = filter()
        
        if result_text == 'profanity found':
            chat = '*'*len(result_text)
            conversation.append(chat)
            point1 = 0
        elif result_text == None:
            break
        else:
            conversation.append(result_text)
            point1 = random.randint(10, 134)
            point2 = random.randint(10, 134)

    convo_joined = ' '.join(conversation)
    backend.chat_block(user_1, user_2, point1, point2, convo_joined)
    print()
    backend.local_blockchain.print_blocks()



    


    

print(beta_convo())