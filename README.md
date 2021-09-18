# Profanity Filter 🎤✅

The Algorithm behind our Ethical Profanity Filter to Keep the convos positive and ethical.

# Functionality ⚙️

The algorithm is based off the naive pattern search algorithm. Given a list of bad words, the algorithm will check every word that the user has typed against each word in the list.
If the word from the "bad words list", the user will be restricted from sending that message, and may have to type the message again in a more positive way. 

Note: The list of bad words is not against anything, or anyone. These words are a dataset of the most common disrespectful words used, and may be used for our comparisions in the alogrithm.

Time Complexity: `O(n * k)` 
 - `n` = length of the list of bad words.
 - `k` = length of the user input.
 
# Limitaions 🌃

The only limitation in this algorithm is that sometimes, the words you want to use in a positive aspect may be blocked due to the natural behaviour of the pattern seearch algorithm. Because of this, the user may be restricted, and if so, may have to re-phrase their message in another way.




 


