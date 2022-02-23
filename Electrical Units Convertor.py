# This Program Converts basic electrical engineering units
# --------Sinusoidal Waves----------------:
# Avg = 0.637 x maximum value
# Rms = 0.707 x maximum value
# Peak to peak = 2 x maximum value
# Three phase value = 1.732 x single phase value

# ----------------------------------------:

num1 = None #
num2 = None
num3 = None
num4 = None
num5 = None


print(' This Program Converts basic electrical engineering units,Mainly Current and Voltage')
print(' Type Y to compute or N to jump the next execution')
print('To End the program type "0 " on the last input')
print('On the first program execution: Type AVG to compute average values ')
print('On the first program execution: Type RMS to compute root means square values ')
print('On the first program execution: Type PEAK  to compute peak to peak values ')
print('On the first program execution: Type 3PHASE  to compute three phase  values ')
print('On the first program execution: Type NULL  to terminate three phase  values ')


try:

    while True:
        userInput = str(input('Would like to compute Average ,Root Means Squa'
                              're, Peak or Three Phase Current or Voltage'))
        if userInput == " AVG ":
            num1 = float(input('Enter the value'))
        elif userInput == " RMS ":
            num2 = float(input('Enter a Number 2'))
        elif userInput == "PEAK":
            num3 = float(input('Enter a Number 3'))
        elif userInput == "3Phase":
            num4 = float(input('Enter a Number 4'))
        elif userInput == "NULL":
            break
        print('Done, Nonthing to compute')

except:
        print("Invalid input")



numArray = [num1, num2, num3, num4]

#calculation of min, max & average

# calculation of min

x_min = min(numArray)

y_max = max(numArray)

z_avg = sum(numArray)/len(numArray)


#calculation
numAvg = 0.637*num1
numRMS = 0.707*num2
numPeak = 2*num3
numThreephase = 1.732 * num4


print(" The average value :", round((numAvg),4))
print("The RMS value : ",round((numRMS),4))
print("The Peak-to-peak :", round(numPeak,4))
print("The Three-phase :", round(numThreephase,4))
