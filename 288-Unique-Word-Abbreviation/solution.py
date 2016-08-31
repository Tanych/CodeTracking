class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.word_dict={}
        for word in dictionary:
            key=self.create_key(word)
            self.word_dict[key]=self.word_dict.get(key,[])+[word]

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        key=self.create_key(word)
        # no abbrivation
        if len(key)< 3:
            return True
            
        if key not in self.word_dict:
            return True
        else:
            #if the word list has only one iterm
            if len(self.word_dict[key]) ==1 and word in self.word_dict[key]:
                return True
        return False
        
    def create_key(self,word):
        if not word:
            return ""
        if len(word)< 3:
            return word
        return word[0]+str(len(word)-2)+word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")