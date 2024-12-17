name1=input("請輸入第一位學生的姓名: ") # 輸入第一位同學的姓名
score1=int(input("\n請輸入第一位學生的成績: ")) # 輸入第一位同學的成績
name2=input("\n請輸入第二位學生的姓名: ") # 輸入第二位同學的姓名
score2=int(input("\n請輸入第二位學生的成績: ")) # 輸入第二位同學的成績
print("\n姓名    成績") # 列印姓名   成績
print("%3s %5d"%(name1,int(score1))) # 列印第一位同學姓名   成績
print("%3s %5d"%(name2,int(score2))) # 列印第二位同學姓名   成績
total=score1+score2
print("成績總分為: "+str(total)) # 列印兩位同學的成績加總分數