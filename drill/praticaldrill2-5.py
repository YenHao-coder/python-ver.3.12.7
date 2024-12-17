cm=int(input("請輸入你的身高(cm): ")) # 請輸入你的身高(cm):
kg=int(input("\n請輸入你的體重(kg): ")) # 請輸入你的體重(kg):
bmi=float(kg/((cm/100)**2))
bmi=('%.2f'%bmi)
print("身高 {} 公分，體重 {} 公斤，BMI值為 {}".format(str(cm), str(kg), str(bmi))) # 身高 cm 公分，體重 kg 公斤，BMI值為 BMI