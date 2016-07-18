class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # deal with 0
        if divisor==0:
            return -1
        # max int overflow
        if dividend==-(1<<31) and divisor==-1:
            return (1<<31)-1
            
        if dividend==0:
            return 0
        if divisor==1:
            return dividend
        if divisor==-1:
            return -dividend
            
        # deal with neg
        neg=-1 if (dividend<0)^(divisor<0) else 1
        dvd_in=abs(dividend)
        dos_in=abs(divisor)
            
        res=0
        while dvd_in>=dos_in:
            # found the first num 
            tmp=dos_in
            mutip=1
            # double dos_in to find the nearest value
            while dvd_in>=(tmp<<1):
                # continue double
                """
                5 1
                10 2
                20 4
                40 8
                80 16
                160 32
                320 64
                640 128
                1280 256
                2560 512
                5120 1024
                10240 2048
                20480 4096
                40960 8192
                81920 16384
                163840 32768
                327680 65536
                655360 131072
                1310720 262144
                2621440 524288
                5242880 1048576
                10485760 2097152
                20971520 4194304
                41943040 8388608
                83886080 16777216
                167772160 33554432
                335544320 67108864
                671088640 134217728
                """
                tmp<<=1
                mutip<<=1
                
            dvd_in-=tmp
            res+=mutip
        return res*neg
            