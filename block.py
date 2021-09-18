import datetime
from hashlib import sha256 

class Block:
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now().strftime('%m/%d/%Y')
        self.transactions = transactions
        self.previous_hash = previous_hash 
        self.nonce = 0 
        self.hash = self.generate_hash()

    
    def generate_hash(self):
        block_header = str(self.time_stamp)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()


    def print_contents(self):
        print("Time Stamp: {}".format(self.time_stamp))
        print("Details of Conversation: {}".format(self.transactions))
        print("Current Hash: {}".format(self.generate_hash()))
        print("Previous Hash: {}".format(self.previous_hash))
