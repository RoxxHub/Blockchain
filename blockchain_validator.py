import hashlib
import pandas as pd
chain = pd.read_csv('rc.csv', index_col=[0])

difficulty = 0

class adder:
    def __init__(self, prev_hash, nonce, *transactions):
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.transactions = transactions
        self.nt = ''
        for i in transactions:
            self.nt += i
        self.hasin = prev_hash + self.nt + str(nonce)
        self.hash = hashlib.sha256(self.hasin.encode()).hexdigest()

        #validating and preparing the block IF is found valid

        if prev_hash == chain.iloc[-1, -1] and self.hash.startswith('0' * difficulty):
            uh = {'s.no': [len(chain) + 1],
                  'nonce': [nonce],
                  'txn': [transactions],
                  'ph': [prev_hash],
                  'h': [self.hash]}
            self.newblock = pd.DataFrame(uh)

        else:
            print('sorry wrong inputs')
            quit()

    def generate(self):
        a = pd.concat([chain, self.newblock], ignore_index=True) # adding it to the chain
        a.to_csv('rc.csv')
        return a

# adding and validating
t1 = '35 rc from tony to steve'
t2 = '20 rc from may to steve'

newchain = adder('694f79a78fb00c7782fa464214e178d0e4f9c2a15130432918c7000ebdc581f0', 3, t1, t2).generate()
