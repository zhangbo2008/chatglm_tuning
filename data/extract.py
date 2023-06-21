import json #读入https://github.com/zhangbo2008/KdConv 数据,把他转化为标注数据集.
with open('data/film/train.json', 'r') as f:
    s1 = json.load(f)
save=[]
for i in s1:
    a=i['messages']#里面的所有对话.
    asks=[]
    answs=[]
    ans=''
    ask=''
    for dex,j in enumerate(a):

        if len(j)==1 :#碰到1就存.
            asks.append(ask)
            answs.append(ans)
            ans=''
            ask=j['message']
        if len(j)==2:
            ans+=j['message']#否则就一直叠加答案.
        if  dex==len(a)-1:#最后一个了也进行提交.
            asks.append(ask)
            answs.append(ans)
    print(1)
            
print(1)