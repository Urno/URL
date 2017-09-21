#텍스트 속의 단어 개수를 확인하는 프로그램
f=open('text2.txt', 'r')
D={};N={};order=[]
for line in f:
    sentence=line.split()
    for k in range(len(sentence)-1) :
        if sentence[k] not in D: D[sentence[k]]=1
        else : D[sentence[k]]+=1
print(D)
for x,n in D.items():
    if n not in N:
        N[n]=[]
        N[n].append(x)
    else : N[n].append(x)
for k in N.keys():
    order.append(k)
order.sort(reverse=True)
for m in order:
    L=", ".join(N[m])
    if len(N[m])==1 : print("Number of word, %s in text, is %d" % (L, m))
    else : print("Number of words, %s in text, are %d" % (L, m))
