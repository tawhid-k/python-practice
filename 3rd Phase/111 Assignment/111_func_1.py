def calBMI(height, weight):
    bmi = weight / (height * height)
    if bmi < 18.5:
        print("Score is " + str(bmi) + ". You are Underweight")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("Score is " + str(bmi) + ". You are Normal")
    elif bmi >= 25 and bmi <= 30:
        print("Score is " + str(bmi) + ". You are Overweight")
    else:
        print("Score is " + str(bmi) + ". You are Obese")

n = input().replace('(', '')
n = n.replace(')', '')

n = n.split(', ')

height = float(n[0])/100
weight = float(n[1])



calBMI(height, weight)

