print("BMI CALCULATOR")
weight=float(input("Please enter your weight (in kg) : "))
height=float(input("Please enter your height (in m) : "))
BMI=weight/height**2
print("Your BMI is : " , BMI)
BMI=float(input("Please enter your BMI : "))
if(BMI<=18.5):
    print("You are underweight")
elif(18.5<BMI<=25):
    print("You have a normal weight")
elif(25<BMI<=30):
    print("You are overweight")
elif(30<BMI<=35):
    print("You are obese")
else:
    print("You are clinically obese")