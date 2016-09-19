# Metric-Imperial-Units

###------------------------FUNCTION DICTIONARY----------------------------###

def wholeLoop():
    repeatStructure = input("Hello again! It's me Neel!\n I hope you enjoyed \
                    the simulation.\nDid you want to try something else? ")
    while repeatStructure != ("Yes" or "yes" or "YES" or "y" or "No" or "no" or "NO" or "n"):
        repeatStructure = input("""Sorry, I didn't get that. Can you try entering that in again?
I was wondering if you wanted to do something else with the simulation?\n """)
        if repeatStructure in ("Yes", "yes", "YES", "y"):
            userChoice = input("""You will now be taken back to the beginning!
Please enter in '1' to convert units from US to UK, and '2' to convert units from UK to US! Thanks!""")
            return userChoice
            break
        elif repeatStructure in ("No", "no", "NO", "n"):
            return repeatStructure
            break


### For selection 1 ###
def convToKmeters():
    _miles = float(input("Now, please enter the number of miles\n\
you'd like to convert into kilometers: "))
    while type(_miles) != float:
        _miles = float(input("Sorry! That's not an actual number.\n\
Please try entering that in again: "))
    milesToKmeters = _miles * 1.6
    print("\n[Zach:] Hey " + userName + " it feels like\n"
            "we've been driving quite a bit.\n"
            "How many kilometers do you think we've\n"
            "gone?\n")
    print("[" + userName + ":] Well it looks like we've been driving\n"
            + str(_miles) + " miles, so that's about\n"
            + str(milesToKmeters) + " kilometers.\n")
    return _miles
    return milesToKmeters

def convToCelsius():
          degFahr = float(input("Now, please enter the degress in fahrenheit\n \
that you'd like to convert into celsius: "))
          while type(degFahr)!= float:
              degFahr = float(input("Sorry! That's not an actual number.\n Please \
             try entering that in again: "))
          fahrToCelsius = (degFahr-32)*(5/9)
          print("\n[Zach:] Man it pretty nice out here!\n"
                "What would this temperature be in\n"
                "Celsius?\n")
          print("[" + userName + ":] Well according to this weather app "
                    "it looks like it's " + str(degFahr) +
                    "\ndegrees Fahrenheit, and " + str(fahrToCelsius) +
                    "\ndegrees Celsius.\n")
          return degFahr
          return fahrToCelsius

def convToLiters():
        _gallons = float(input("Now, please enter the number of gallons\n \
that you'd like to convert into liters: "))
        while type(_gallons) != float:
                    _gallons = float(input("Sorry! That's not an actual number. Please\n \
                         try entering that in again: "))
        gallonsToLiters = (_gallons)*(3.9)
        print("\n[Zach:] Dang, that looks like a lot of water!"
                    "Do you think you could tell me how many"
                    "liters of water that is?")
        print("[" + userName + ":] Well it says here that it's about \n"
                    + str(_gallons) + " gallons which must mean that\n"
                    "it's around " + str(gallonsToLiters) + " liters!\n")
        return _gallons
        return gallonsToLiters

def convToKgrams():
          _pounds = float(input("Now, please enter the number of pounds\n \
that you'd like to convert into kilograms: "))
          while type(_pounds) != float:
                     _pounds = float(input("Sorry! That's not an actual number. Please\n \
                         try entering that in again: "))
          poundsToKgrams = _pounds*(0.45)
          print("\n[Zach:] Wow, I almost thought I gained some\n"
                                "weight when I stepped onto your scale!\n"
                                "Do you think you could tell me how much\n"
                                "I weight in kilograms based of how it reads?\n")
          print("[" + userName + ":] Well it says that you weigh " + str(_pounds) +
                                "\n pounds, and that must mean you weigh\n"
                                + str(poundsToKgrams) + " in kilograms!\n")
          return _pounds
          return poundsToKgrams

def convToCmeters():
           _inches = float(input("Now, please enter the number of inches\n \
that you'd like to convert into centimeters: "))
           while type(_inches) != float:
                 _inches = float(input("Sorry! That's not an actual number. Please\n \
                         try entering that in again: "))
           inchesToCmeters = _inches*(2.54)
           print("\n[Zach:] You know what's weird is that actually\n"
                                "prefer inches to centimeters? But I still\n"
                                "can't figure out how long that is in\n"
                                "inches!\n")
           print("[" + userName + ":] Well I'd say that's got to be\n"
                                + str(_inches) + " inches, which means it's\n"
                                "definitely " + str(inchesToCmeters)+ " centimeters!\n")
           print("[Zach:] Thanks for all of your help " + userName + "!")
           return _inches
           return _inchesToCmeters

def path1():
    print("""Great choice! The simulation will begin after
after a quick tap of your 'enter' key.""")
    input("")
    print("----------SIMULATION----------")
    print("[" + userName + ":] Hello Zach! Welcome to the US!")
    print("[Zach:] Hello " + userName + " it's good to be here!\n"
                "The only thing is that I forgot that you\n"
                "guys use the imperial system over here.\n")
    print("[" + userName + ":] I can't even begin to understand\n"
                "why anyone would use anything different.\n"
                "But since you are family, would you like\n"
                "it if I helped you convert some units?\n")
    print("[Zach:] That would be great! Thank you!\n")
    convToKmeters()
    print("\n")
    convToCelsius()
    print("\n")
    convToLiters()
    print("\n")
    convToKgrams()
    print("\n")
    convToCmeters()
    print("\n\n")



### For selection 2 ###
def convToMiles():
    kmeters = float(input("Now, please enter the number of kilometeres\n\
you'd like to convert into miles: "))
    while type(kmeters) != float:
        kmeters = float(input("""Sorry! That's not an actual number.
Please try entering that in again: """))
    kmetersToMiles = 0.625 * kmeters
    print("\n[Jim:] Hey " + userName + " it feels like\n"
            "we've been driving quite a bit.\n"
            "How many miles do you think we've\n"
            "gone?\n")
    print("[" + userName + ":] Well it looks like we've been driving\n"
            + str(kmeters) + " kilometers, so that's about\n"
            + str(kmetersToMiles) + " miles.\n")
    return kmeters
    return kmetersToMiles

def convToFahr():
    degCelsius = float(input("Now, please enter the degress in Celsius\n \
that you'd like to convert into Fahrenheit: "))
    while type(degCelsius)!= float:
        degCelsius = float(input("Sorry! That's not an actual number.\n Please \
             try entering that in again: "))
    celsiusToFahr = degCelsius*(9/5) + 32
    print("\n[Jim:] Man it pretty nice out here!\n"
                "What would this temperature be in\n"
                "Fahrenheit?\n")
    print("[" + userName + ":] Well according to this weather app "
                    "it looks like it's " + str(degCelsius) +
                    "\ndegrees Fahrenheit, and " + str(celsiusToFahr) +
                    "\ndegrees Celsius.\n")
    return degCelsius
    return celsiusToFahr

def convToGallons():
    _liters = float(input("Now, please enter the number of liters\n \
that you'd like to convert into gallons: "))
    while type(_liters) != float:
            _liters = float(input("Sorry! That's not an actual number. Please\n \
                         try entering that in again: "))
    litersToGallons = (_liters)*(1/(3.9))
    print("\n[Jim:] Dang, that looks like a lot of water!"
                    "Do you think you could tell me how many"
                    "gallons of water that is?")
    print("[" + userName + ":] Well it says here that it's about \n"
                    + str(_liters) + " liters which must mean that\n"
                    "it's around " + str(litersToGallons) + " gallons!\n")
    return _liters
    return litersToGallons

def convToPounds():
    kgrams = float(input("Now, please enter the number of kilograms\n \
that you'd like to convert into pounds: "))
    while type(kgrams) != float:
                 kgrams = float(input("Sorry! That's not an actual number. Please\n \
                         try entering that in again: "))
    kgramsToPounds = kgrams*(1/(0.45))
    print("\n[Jim:] Wow, I almost thought I lost some\n"
                "weight when I stepped onto your scale!\n"
                "Do you think you could tell me how much\n"
                "I weight in pounds based of how it reads?\n")
    print("[" + userName + ":] Well it says that you weigh " + str(kgrams) +
                        "\n kilograms, and that must mean you weigh\n"
                        + str(kgramsToPounds) + " in pounds!\n")
    return kgrams
    return kgramsToPounds

def convToInches():
    cmeters = float(input("Now, please enter the number of centimeters\n \
that you'd like to convert into inches: "))
    while type(cmeters) != float:
                 cmeters = float(input("Sorry! That's not an actual number. Please\n \
                         try entering that in again: "))
    cmetersToInches = cmeters*(1/(2.54))
    print("\n[Jim:] You know what's weird is that actually\n"
                    "prefer centimeters to inches? But I still\n"
                    "can't figure out how long that is in\n"
                    "centimeters!\n")
    print("[" + userName + ":] Well I'd say that's got to be\n"
                         + str(cmeters) + " centimeters, which means it's\n"
                        "definitely " + str(cmetersToInches) + " inches!\n")
    print("[Jim:] Thanks for all of your help " + userName + "!")
    return cmeters
    return cmetersToInches

def path2():
    print("""Great choice! The simulation will begin after
after a quick tap of your 'enter' key.""")
    input("")
    input("\n")
    print("----------SIMULATION----------")
    print("[" + userName + ":] Hello Jim! Welcome to the UK!")
    print("[Jim:] Hello " + userName + " it's good to be here!\n"
                "The only thing is that I forgot that you\n"
                "guys use the metric system over here.\n")
    print("[" + userName + ":] I can't even begin to understand\n"
                "why anyone would use anything different.\n"
                "But since you are family, would you like\n"
                "it if I helped you convert some units?\n")
    print("[Jim:] That would be great! Thank you!\n")
    convToMiles()
    print("\n")
    convToFahr()
    print("\n")
    convToGallons()
    print("\n")
    convToPounds()
    print("\n")
    convToInches()
    print("\n\n")



###---------------------------------INTRO---------------------------------###


### Program Greeting ###
print("""Hello! Welcome to your personal and friendly conversion terminal.\n
      This terminal can be used to convert US and UK units to one another.\n
      Please press enter when you're ready to get started, and then just\n
      follow the on-screen prompts!\n\n\n""")

input(" \n")

### Retreiving user's name ###
global userName
userName = input("Hello, my name is Neel! What's yours? ")

print("\nHello " + userName + " it's nice to meet you!")


### Exlanation of simulation setting and dialougue ###
print("""Next, I need you to decide whether you want to convert your units
        of measurement from US to UK or from UK to US. Based on which one
        you choose, a simulation will start in which your cousin is visiting
        you from their home country of either the US or the UK, and you need
        to convert the units from the country their visiting to the units of
        their country!\n""")

### Deciding how to convert the units ###

userChoice = input("""If you wish to convert units from US to UK please
enter '1', and if you wish to convert units from UK to US please enter '2'.\n""")



### Initializing the variable that helps to loop over the entire main program ###
repeatStructure = "yes"

###----------------------------------BODY---------------------------------###

while repeatStructure in ("Yes", "yes", "YES", "y"):
      if userChoice == "1":
          while userChoice == "1":
              print("""\nYou've chosen to convert units from US to UK!
Is this what you meant to select?\n""")
              verifyPath1 = input("Please enter 'no' to start over and 'yes' to continue. ")
              if verifyPath1 in ("yes", "Yes", "YES", "y"):
                  path1()
                  wholeLoop()
              elif verifyPath1 in ("No", "no", "NO", "n"):
                  userChoice = input("I'm sorry about that, please enter in your conversion\n\
choice again! As a reminder, it's '1' for US to UK,\n\
and '2' for UK to US again.")
      elif userChoice == "2":
          while userChoice == "2":
              print("""You've chosen to convert units from UK to US!
Is this what you meant to select?\n""")
              verifyPath2 = input("Please enter 'no' to start over and 'yes' to continue. ")
              if verifyPath2 in ("yes", "Yes", "YES", "y"):
                  path2()
                  wholeLoop()
              elif verifyPath2 in ("No", "no", "NO", "n"):
                  userChoice = input("I'm sorry about that, please enter in your conversion\n\
choice again! As a reminder, it's 1 for US to UK,\n\
and 2 for UK to US again.")
      elif userChoice != ("1" or "2"):
          while userChoice != ("1" or "2"):
              print(userChoice)
              userChoice = input("Sorry " + userName + """! Unfortunately that's not an available
choice. Please try entering that in again. Remember your choices
for this simulation are '1' for conversion from US to UK and '2' for UK to US.\n""")


print("""Thanks for visiting! I appreciate you taking the time to use our
simulator, and I hope that you come back again soon!\n\n
Sincerely, Neel Agarwal""")
