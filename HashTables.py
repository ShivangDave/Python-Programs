class HashTables:
    def __init__(self,size=100):
        self.hashTable = [[] for _ in range(size)]
        self.size = size

    def hashKey(self,key):
        return hash(key) % len(self.hashTable)

    def insertCollision(self,key,value):
        # Doesn't Prevent Collision
        hashedKey = self.hashKey(key)
        self.hashTable[hashedKey] = value

    def insert(self,key,value):
        # Collision Proofing using Chaining
        hashedKey = self.hashKey(key)
        key_exist = False
        sublist = self.hashTable[hashedKey]

        if self.hashTable is not [None]*self.size:
            for i, kv in enumerate(sublist):
                k, v = kv
                if key == k:
                    key_exist = True
                    break
            if key_exist:
                sublist[i] = ((key,value))
            else:
                sublist.append((key,value))
        else:
            self.hashTable[hashedKey] = (key, value)

    def sizeOfTable(self):
        return len(self.hashTable)

    def search(self,key):
        hashedKey = self.hashKey(key)
        sublist = self.hashTable[hashedKey]
        for i,kv in enumerate(sublist):
            k, v = kv
            if key == k:
                return v

    def delete(self,key):
        hashedKey = self.hashKey(key)
        key_exist = False
        sublist = self.hashTable[hashedKey]

        for i, kv in enumerate(sublist):
            k, v = kv
            if key == k:
                key_exist = True
                break
        if key_exist:
            return sublist.pop(i)
            #del sublist[i]
        else:
            print("Key not found!")
