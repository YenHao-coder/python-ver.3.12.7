student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
# 練習題: 轉換學生分數為成績

# 建立學生成績字典: 學生名字為 "Key"; 評估成績為 "Value"

# 評分標準: 分數 91-100: 評級 "Outstanding",分數 81-90: 評級 "Exceeds Expectations", 分數 71-80: 評級 "Acceptable", 分數 70及以下: 評級 "Fail"

student_grades = {}

for grade in student_scores:
    if student_scores[grade] >= 91:
        student_grades[grade] = "Outstanding"
    elif student_scores[grade] >= 81:
        student_grades[grade] = "Exceeds Expectations"
    elif student_scores[grade] >= 71:
        student_grades[grade] = "Acceptable"
    else:
        student_grades[grade] = "Fail"

print(student_grades)