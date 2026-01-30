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
