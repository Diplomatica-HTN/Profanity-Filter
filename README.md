# Profanity Filter 🎤✅

The Algorithm behind our Ethical Profanity Filter to Keep the convos positive and ethical.

# Functionality ⚙️

The algorithm is based off the naive pattern search algorithm. Given a list of bad words, the algorithm will check every word that the user has typed against each word in the list.
If the word from the "bad words list", the user will be restricted from sending that message, and may have to type the message again in a more positive way. 

Note: The list of bad words is not against anything, or anyone. These words are a dataset of the most common disrespectful words used, and may be used for our comparisions in the alogrithm.

Time Complexity: `O(n * k)` 
 - `n` = length of the list of bad words.
 - `k` = length of the user input.

# Blockchain ⛓

Our chat system is decentralized as well. After the ending of each conversation (debate), the convo itself will be transformed into a block with a time stamp, and secured with a sha256 hash code. Each conversation will be linked under hash codes and users can retrieve information in constant time by retrieving a conversation hash (the transaction hash code). 

Our local blockchain allows for a secured platform for all users to express their thoughts and learn the truth about events around the world. There is a proof-of-state, and users can try to submit proofs. There is a validation function that checks the work submitted by the user, however, if the user's proof-of-state is incorrect, there is a chance where the whole conversation may break and be separated from the chain itself. In this case, the blockchain resets itself for the user logged in.
 
# Limitations 🌃

The only limitation in this algorithm is that sometimes, the words you want to use in a positive aspect may be blocked due to the natural behaviour of the pattern seearch algorithm. Because of this, the user may be restricted, and if so, may have to re-phrase their message in another way.




 


