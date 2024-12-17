cm=int(input("請問你的身高是幾公分? ")) # 請問你的身高是幾公分? 
inch=int(cm%(2.54*12))
ft=int(cm//(2.54*12))
print("身高 {} 等於 {} 呎 {} 吋".format(str(cm), str(ft),str(inch))) # 身高 公分等於 呎 吋