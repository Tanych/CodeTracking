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
        hashmap=[0]*10
        # count the bulls
        for i in xrange(len(secret)):
            if  secret[i]==guess[i]:
                bulls+=1
            else:
                # if secret match the <
                # it means that the guess has access the map
                if hashmap[int(secret[i])]<0:
                    cows+=1
                # secret to plus the record
                hashmap[int(secret[i])]+=1
                
                # check whether the map is larger than 0
                # if so, the secret must access before
                if hashmap[int(guess[i])]>0:
                    cows+=1
                # guess to plus the record
                hashmap[int(guess[i])]-=1
                
        return str(bulls)+'A'+str(cows)+'B'
        
        