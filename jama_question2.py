#Jama abdiaziz
#Assignment 3 - QUIZ 2
#Description: program that converts temperature 
#from fahrenheit to celcius and determines
#whether it is hot or cold

# function to convert fahrenheit to celcius
def convert(fahrenheit):
  """
  This function takes temperature in fahrenheit and converts
  it to celcius using the formula: C = (5/9) * (F - 32)
  """
  celcius =(5/9) *  (fahrenheit - 32)
  return celcius

#   main program starts here 
print("==== Temperature converter ====")

# ask user for input 
fahrenheit = float(input(input("Enter temperature in fahrenheit:"))

# call the function
celcius = convert(fahrenheit)

#display the converted temperature
print("__________________")
print("Temperature in celcius:", celcius)

# check if it is hot or cold
if celcius > 20:
  print("ITS HOT HERE")
else:
  print("ITS COLD HERE")
print("____________________________")
print("program completed successfully")
