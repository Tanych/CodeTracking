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
        if pos==len(num) and curres==target:
            print prenum,curres,target
            res.append(path)
            return
        strnum=''
        for i in xrange(pos,len(num)):
            # get 0001
            if num[pos]=='0' and i>pos: break
            strnum+=num[i]
            curnum=int(strnum)
            if curnum>(1<<31): break
            if pos==0:
                self.travel(num,target,i+1,path+strnum,curnum,curnum,res)
            else:
                self.travel(num,target,i+1,path+'+'+strnum,curnum,curres+curnum,res)
                # it's -curnum not curnum
                self.travel(num,target,i+1,path+'-'+strnum,-curnum,curres-curnum,res)
                self.travel(num,target,i+1,path+'*'+strnum,prenum*curnum,(curres-prenum)+prenum*curnum,res)
        
       
        
        
        