# 閏年判斷程序
# 如何分辨閏年: 
#   1.可以被4整除
#   2.排除可以被100整除但不排除可以被400整除


def is_leap_year(year):
    # Write your code here.
    if year%400 == 0:
        return True
    elif year%4 == 0 and year%100 != 0:
        return True
    else:
        return False
    # Don't change the function name.
year1 = is_leap_year(int(input("Is it a leap year? ")))
print(year1)

    # Don't change the function name.