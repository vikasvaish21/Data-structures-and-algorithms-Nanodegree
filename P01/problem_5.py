import datetime
import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None


    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = f'{self.timestamp}\n{self.data}.\n{self.previous_hash}'.encode('utf-8')
      sha.update(hash_str)

      return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,value):
        if value is None:
            return
        self.size += 1
        node = self.head


        if node is None:
            block = Block(datetime.datetime.now(),value,None)
            self.head = block
        else:
            while node.next:
                node = node.next
            node.next = Block(datetime.datetime.now(),value,node.hash)

chain = BlockChain()
chain.append('data for a')
chain.append('data for b')
chain.append('data for c')
chain.append(None)
print(chain.head.data)
#print(chain.head.next.data)
#print(chain.head.next.next.data)
b = chain.head.next
c = chain.head.next.next
print(b.hash == c.previous_hash)
print(b.data)
print(c.data)
