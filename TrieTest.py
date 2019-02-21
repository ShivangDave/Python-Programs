from Trie import Trie

root = Trie('*')
root.add(root,'hackathon')
root.add(root,'hack')
root.add(root,'hal')

print(root.findPrefix(root,'hack'))
print(root.findPrefix(root,'ha'))
print(root.findPrefix(root,'hammer'))
