text = input().split()
dictionary = {}
def inDictionary(w):
  if word in dictionary:
    return True
  return False

def addToDictionary(w):
  dictionary[word] = len(dictionary) + 1

for word in text:
  if inDictionary(word):
    print(dictionary[word], end=" ")
  else:
    print(word, end=" ")
    addToDictionary(word)