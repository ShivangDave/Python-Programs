from HashTables import HashTables

# hashTable = HashTables(10)
# hashTable.insertCollision(10,"ih")
# hashTable.insertCollision(20,"Nice")
# hashTable.insertCollision(25,"hole")
#
# print(hashTable.sizeOfTable())
# print(hashTable.hashTable)

hashTable = HashTables(10)

hashTable.insert(10,"ih")
hashTable.insert(20,"Nice")
hashTable.insert(25,"hole")

print(hashTable.sizeOfTable())
print(hashTable.hashTable)

print(hashTable.search(25))
print(hashTable.delete(20))
print(hashTable.hashTable)
#print(hashTable.sizeOfTable())
#print(hashTable.hashTable)
