class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            short,longer = str2,str1
        else:
            short,longer = str1,str2
        gcd = []
        for i in range(len(short)):
            if len(short)%(i+1)==0:
                if short == short[:i+1]*(len(short)//(i+1)):
                    gcd.append(short[:i+1])
        gcd2=[]
        for i in gcd:
            if len(longer)%len(i)==0:
                if longer == i*(len(longer)//len(i)):
                    gcd2.append(i)
        if not gcd2:
            return ''
        return max(gcd2,key=len)