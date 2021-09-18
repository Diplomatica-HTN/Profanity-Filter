from blockchain import Blockchain
import random
from datetime import datetime

class Chat_Backend:
    local_blockchain = Blockchain()

    def chat_block(self, user1, user2, user1_point, user2_point, conversation):
        time = datetime.now().strftime('%m/%d/%Y')
        block = {'user1': user1, 'user2': user2, 'Time of Conversation':time, 'points for user1':user1_point, 'points for user2':user2_point, 'Content':conversation}
        self.local_blockchain.add_block(block)


    
backend = Chat_Backend()


