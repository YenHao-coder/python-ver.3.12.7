salary=int(input("請輸入薪資金額: ")) # 請輸入薪資金額:
bonus=int(input("\n請輸入工作獎金: ")) # 請輸入工作獎金:
pay=int(input('\n請輸入加班費: ')) # 請輸入加班費:
total=sum([salary,bonus,pay])
print("本月實領金額為: "+str(total)) # 本月時領金額為: