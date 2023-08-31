import sys

China = 112385
USA = 81064103
SA = 3688423


def mainMenu():
    print("Welcome to the COVID-19 support service. Please select a service below:")
    a = "1. Statistics"
    b = "2. Prevention"
    c = "3. Symptoms"
    d = "4. Treatment"
    e = "5. Report case"
    f = "6. Exit"
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)


def ReturnMain():
    r = input("")
    if r == "":
        exec()
    else:
        exec()


def Statistics():
    print("")
    print("These are the current cases in the following countries:")
    print("")
    print("Currently in China the amount of cases are:" + "" + str(China) )
    print("Currently in USA the amount of cases are:" + "" + str(USA))
    print("Currently in SA the amount of cases are:" + "" + str(SA))
    print("")


    t= input("Would you like to see the confirmed cases of a random country? yes/no:")

    myList = ["France= 23,234,062", "Afghanistan= 175,525", "Germany= 16,336,336	", "Canada= 3,342,123",
              "Australia= 3,500,734", "India= 42,980,067", "Japan= 5,546,271", "Chad= 7,258", "Italy= 13,159,342",
              "Brazil= 29,194,042"]
    if t == "yes":
        i = int(input("To Select random country , type a number from 0 to 9: "))
        print(myList[i])


    print("Press enter to return to the main menu")
    ReturnMain()

print("")


def Prevention():
    print("")
    print("1. Clean your hands often with soap and water, or an alcohol based hand rub.")
    print("2. Maintain a safe distance from anyone whois coughing and sneezing.")
    print("3. Don't touch your eyes, nose or mouth.")
    print("4. Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.")
    print("5. Stay home if you feel unwell.")
    print("6. If you have a fever, cough and difficulty breathing, seek medical attention. Call in Advance.")
    print("7. Follow the directions of your local health authority ")
    print("Press enter to return to the main menu")
    ReturnMain()


def Symptoms():
    print("")
    print("MOST COMMOM SYMPTOMS INCLUDE:")
    print("Fever")
    print("Cough")
    print("Tiredness")
    print("Loss of taste or smell")
    print("")
    print("LESS COMMON SYMPTOMS INCLUDE:")
    print("Headaches")
    print("Sore throat")
    print("Aches and Pains")
    print("Diarrhoea")
    print("A rash on the skin, discolouration of toes and fingers")
    print("Red or irritated eyes")
    print("")
    print("SERIOUS SYMPTOMS INCLUDE:")
    print("Difficulty breathing or shortness of breath")
    print("Loss of speach, mobility or confusion")
    print("Chest Pain")
    print("")
    print("Press enter to return to the main menu")
    ReturnMain()


def Treatment():
    print("")
    print("After exposure to someone who has COVID-19, please do the following:")
    print("")
    print("1. Fisrt Call your health care provider or COVID-19 hotline to find out where and when to get a test.")
    print("2. Cooperate with contact-tracing procedures that have been put in place to stop the spread of the virus.")
    print("3. If testing is not available at the time, stay home and away from others for 14 days.")
    print(
        "4. While you are in quarantine, you must not go to work, to school or to public places. Ask someone to bring you supplies.")
    print("5. Keep at least a 1.5-metre distance from others, even from your family members.")
    print("6. Wear a medical mask to protect others, including if/when you need to seek medical care.")
    print("7. Clean your hands frequently.")
    print("8. Stay in a separate room from other family members, and if not possible, wear a medical mask.")
    print("9. Keep the room well-ventilated.")
    print("10. If you share a room, place beds at least 1 metre apart.")
    print("11. Monitor yourself for any symptoms for 14 days.")
    print( "12. Call your health care provider immediately if you have any of these danger signs: difficulty breathing, loss of speech or mobility, confusion or chest pain.")
    print("13. Stay positive by keeping in touch with loved ones by phone or online, and by exercising at home.")
    print("")
    print("Press enter to return to the main menu")
    ReturnMain()


def Report_case():
    print("")
    print("Do you have Symptoms?")
    x = input("Please enter yes or no:")
    o = 1
    if x == "yes":
        print("Do you have a temperature above 38.5°C?")
        y = input("Please enter yes or no: ")
        if y == "yes":
            print("In which country are you? Select and option below:")
            print("1. SA")
            print("2. USA")
            print("3. CHINA")
            z = input("Please enter option (1,2,3) ")
            if z == "1":
                sa1 = SA + o
                print("SA's cases are now: " + str(sa1))
                print("You have COVID-19 , please see Treatment")
            elif z == "2":
                usa1 = USA + o
                print("USA's cases are now:" + "" + str(usa1))
                print("You have COVID-19 , please see Treatment")
            elif z == "3":
                china1 = China + o
                print("China's cases are now: " + str(china1))
                print("You have COVID-19 , please see Treatment")




        else:
            print("You Don't have COVID")
    elif x == "no":
        print("You don't have COVID")
        print("")
    print("Press enter to return to the main menu")


    ReturnMain()


def exit():
    print("Thank you for using the Advanced COVID System Program of Awesomness!!!")
    sys.exit()


def exec():
    mainMenu()
    m = input("Enter Choice (1/2/3/4/5/6):")
    if m == "1":
        Statistics()
    elif m == "2":
        Prevention()
    elif m == "3":
        Symptoms()
    elif m == "4":
        Treatment()
    elif m == "5":
        Report_case()
    elif m == "6":
        sys.exit()
    else:
        exec()


exec()

