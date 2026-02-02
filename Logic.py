def BMI(para1, para2)->float:
    height = para1 / 100
    weight = para2
    bmi = weight / (height * height)
    return bmi
    
height = float(input("Please enter your height (cm) => "))
weight = float(input("Please enter your weight (kg) => "))
bmi = BMI(height, weight)
if bmi < 18.5:
    print(f"你的BMI值為 {bmi:.1f}，體重過輕")
elif bmi < 24:
    print(f"你的BMI值為 {bmi:.1f}，體重正常")
elif bmi < 27:
    print(f"你的BMI值為 {bmi:.1f}，體重過重")
else:
    print(f"你的BMI值為 {bmi:.1f}，體重肥胖")



'''if i > 5:
    break
if i % 2 == 0:
    continue'''
'''
var1 = 9
if var1 >= 20:
    print("this condition is true")
elif var1 >= 10:
    print("this condition is true")
elif var1 >= 5:
    print("this condition is true")
elif var1 >= 1:
    print("this condition is true")
elif var1 >= -1:
    print("this condition is true")
else:
    print("conditions are false")'''
'''for i in range(1, 11):
    print("i = " + str(i))
i = 1
while i <= 10:
    print("i = " + str(i))
    i = i + 1
if i > 5:
    break
if i % 2 == 0:
    continue
'''

