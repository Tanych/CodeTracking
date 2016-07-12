class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n=len(secret)
        bulls=0
        cows=0
        secret_left=[]
        guess_left=[]
        # count the bulls
        for i in xrange(len(secret)):
            if  secret[i]==guess[i]:
                bulls+=1
            else:
                secret_left.append(secret[i])
                guess_left.append(guess[i])
        
        # count the intesection of two list
        hashmap={}
        for num in secret_left:
            hashmap[num]=hashmap.get(num,0)+1
        
        for num in guess_left:
            hashmap[num]=hashmap.get(num,0)-1
            if hashmap[num]>=0:
                cows+=1
                
        return str(bulls)+'A'+str(cows)+'B'
        
        