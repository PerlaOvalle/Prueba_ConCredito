def split(word): 
    return [char for char in word]
 
def anagrama(word1, word2):
    word1 = word1.lower()
    word1 = split(word1)
    word1 = sorted(word1)
    word2 = word2.lower()
    word2 = split(word2)
    word2 = sorted(word2)
    if word1 == word2:
        return True
    return False
    
print(anagrama("roma", "amor"))