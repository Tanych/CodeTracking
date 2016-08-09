class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        """
        It's typical backtracking problem, but we need pay attention to the corner case 
        EX: 0001+2 it's not valid and the 2+3*4, we can't deal with (2+3)*4 since no ()
        """
        res=[]
        if len(num)==0:
            return res
            
        self.travel(num,target,0,"",0,0,res)
        return res
        
    def travel(self,num,target,pos,path,prenum,curres,res):
        # find one solution
        if pos==len(num) and curres==target:
            res.append(path)
            return
        
        for i in xrange(pos,len(num)):
            # get rid of the '0'
            if num[pos]=='0' and i>pos:break
            # substring
            strnum=num[pos:i+1]
            curnum=long(strnum)
            
            if pos==0:
                self.travel(num,target,i+1,path+strnum,curnum,curnum,res)
            else:
                self.travel(num,target,i+1,path+'+'+strnum,curnum,curres+curnum,res)
                self.travel(num,target,i+1,path+'-'+strnum,-curnum,curres-curnum,res)
                # it's more complicated, 2+3*4, curres--5,prenum--3, the result would
                # (5-3)+3*4, if it's 2*3*4-->prenum is 2*3 (2*3-2*3)+2*3*4
                self.travel(num,target,i+1,path+'*'+strnum,prenum*curnum,(curres-prenum)+prenum*curnum,res)
        
       
        
        
        