temperature = 50
if temperature > 80 or temperature < 60:
    print("Stay inside!")
else:
    print("Enjoy the outdoor!")

print("------------------------")

forecast = "rainy"
if temperature < 80 or forecast != "rainy":
    print("Go outside!")
else:
    print("Stay inside!")

print("------------------------")

forecast2 = "sunny"
if temperature < 80 and forecast2 != "rainy":
    print("Go outside!")
else:
    print("Stay inside!")

print("------------------------")

if not forecast == "rainy":
    print("Go outside!")
else:
    print("Stay inside!")

print("------------------------")

raining = True
if not raining:
    print("Go outside!")
else:
    print("Stay inside!")