#BMI is a measure of relative weight based on an individual’s
#mass and height. Today, Body Mass Index is commonly used to
#classify people as underweight, overweight, and even with obesity.
#Also, it is adopted by countries to promote healthy eating.




print('BMI Calculator')


height = float (input('Enter your height in centimeters:\n'))
weight = float (input('Enter your weight in Kilograms:\n'))

height = height/100
Bodymaxindex = weight/(height*height)
print('Your Body Mass Index is: ',Bodymaxindex)

if(Bodymaxindex>0):
        if (Bodymaxindex <= 16):
            print("you are severely underweight")
        elif (Bodymaxindex <= 18.5):
            print("you are underweight")
        elif (Bodymaxindex <= 25):
            print("you are Healthy")
        elif Bodymaxindex <= 30):
            print("you are overweight")
        else:
            print("you are severely overweight")
    else:
        ("enter valid details")
