bool isHappy(int n) {
    int nDigtal[10]={0};
    int sum=0;
    int sumArray[50]={0};
    int nCount=0;
    do
    {
        memset(nDigtal,0,sizeof(int)*10);
        int nPos=0;
        sum=0;
        while(n!=0)
        {
                nDigtal[nPos]=n%10;
                n/=10;
                nPos++;
        }
        for(int i=0;i<10;i++)
        { 
            sum+=nDigtal[i]*nDigtal[i];//printf("%d,",nDigtal[i]);
        }
        for(int i=0;i<50;++i)
        {
                if(sum==sumArray[i])
                    return false;
        }
        sumArray[++nCount]=sum;
        //printf("\n");
        n=sum;
    }while(sum!=1);

    return true;
    
}