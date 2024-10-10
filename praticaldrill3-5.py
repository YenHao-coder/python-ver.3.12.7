Ce=int(input('請輸入一個西元年: ')) #請輸入一個西元年: 
if (Ce%100!=0) and (Ce%4==0):
    print('西元 '+str(Ce)+' 年是閏年')
elif (Ce%100==0) and (Ce%400==0):
    print('西元 '+str(Ce)+' 年是閏年')    
else:
    print('西元 '+str(Ce)+' 年不是閏年') #西元 年是/不是閏年