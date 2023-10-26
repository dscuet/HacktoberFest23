
#Author: Abdul Sabur
#URL: https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true
def Encryption(ar):
    # Write your code here
    a=s.replace(" ","")
    l=len(a)
    x=math.sqrt(l)
    r=math.floor(x)
    c=math.ceil(x)
    start=0
    end=c
    b=[]
    
    if r * c < l:
        r += 1
        
    for i in range(r):
        b.append(a[start:end])
        start=end
        end+=c
    d=[]
    for col in range(c):
        d.append("".join([row[col] for row in b if col<len(row)]))
    return " ".join(d)

