# Program to check if the temperature is suitable for light clothes

temperature = int(input("Enter the temperature in °C: "))

if temperature >= 20 and temperature <= 30:
    print("It's suitable for wearing light clothes.")
elif temperature > 30:
    print("It's hot! Light clothes are definitely fine.")
else:
    print("It's too cold. Better wear something warmer.")
