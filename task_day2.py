 # 數據型態
print("Hello"[0:3]) #字元位置0不包含3
 #字串運算
print('123'+'456')
 #整數
print(123 + 456)
print(123_456_789)
# 浮點數
print(3.14159)
# 布林值
print(True)
print(False)
# 資料型態轉換
type('Hello')  #判斷哪種資料型態
print(type(123)) #整數型態
print(type('abc')) #字串型態
print(type(2.653)) #浮點數型態
print(type(True)) #布林值
print('Nnmber of letters in your name: '+str(len(input('Enter your name ')))) #資料型態錯誤改正
#數值運算子: +, -, *, /除以, //除, **次方, %餘
print(3*3+3/3-3)
# BMI 計算器
bmi = 84/1.65**2
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))
# 複合指定運算子 *=, -=, +=, /=
# f-字串: 插入整數等資料型態轉為字串並列印
print(f"Your bmi is {bmi}")
# 小費計算機
print("歡迎使用小費計算器! \n")
bill = float(input("請輸入帳單金額: $")+)
tip = float(input('請輸入小費費率? 10, 12, 或 15? '))
percentage = tip/100
number_people = int(input('請輸入多少人付款? '))
bill_per_person = bill*(1+percentage)/number_people
print(f'每位客人應付: {round(bill_per_person, 2)} 元')