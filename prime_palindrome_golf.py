__author__ = 'Vegh Adam'

def golf(n):
 while(str(n+1)!=str(n+1)[::-1])|([k for k in range(2,n+1)if(n+1)%k==0]!=[]):n+=1
 return n+1