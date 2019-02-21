class HashMap:
    def __init__(self,size=10):
        self.size = size
        self.map = [None] * self.size

    def getHash(self,key):
        return hash(key) % len(self.map)

    def add(self,key,value):
        keyHash = self.getHash(key)
        keyValue = [key, value]

        if self.map[keyHash] is None:
            self.map[keyHash] = list([keyValue])
            return True
        else:
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
                self.map[keyHash].append(keyValue)
                return True

    def get(self,key):
        keyHash = self.getHash(key)
        if self.map[keyHash] is not None:
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self,key):
        keyHash = self.getHash(key)
        if self.map[keyHash] is None:
            return False
        for i in range(0,len(self.map[keyHash])):
            if self.map[keyHash][0] == key:
                self.map[keyHash].pop(i)
                return True

    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))
