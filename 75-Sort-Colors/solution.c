void sortColors(int* nums, int numsSize) {
    int redcnt=0;
    int whitecnt=0;
    int bluecnt=0;
    
    for(int i=0;i<numsSize;++i)
    {
        switch(nums[i])
        {
            case 0:
                redcnt++;
                break;
            case 1:
                whitecnt++;
                break;
            default:
                bluecnt++;
                break;
        }
    }
    //---red--
    for(int i=0;i<redcnt;++i)
    {
        nums[i]=0;
    }
    //--white--
    for(int i=redcnt;i<redcnt+whitecnt;++i)
    {
        nums[i]=1;
    }
    //---blue--
    for(int i=redcnt+whitecnt;i<redcnt+whitecnt+bluecnt;++i)
    {
        nums[i]=2;
    }
}