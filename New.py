class activity:

    def activity1(self):
        print("\nYou must be sitting")

    def activity2(self):
        print("\nSit down if you're tired! You should take a nap")

    def activity7(self):
        print("\nYou're standing")

    def activity3(self):
        print("\nYou're Walking, It's good for health")

    def activity4(self):
        print("\nYou're Running and it's really good to keep exercising in this Quarantine")

    def activity5(self):
        print("\nWhy are you Sad, just get up and Pray")

    def activity6(self):
        print("\nI'm unable to recognize what you're doing, May Allah protect you")

    def activity8(self):
        print("\nMay Allah give you sabar")


obj = activity()

choice = 1

while choice != 0:

    print("\n PHYSICAL ACTIVITY RECOGNITION AGENT\n")

    print("1. Tired \n")

    print("2. Yawning \n")

    print("3. Motivated to loose some weight \n")

    print("4. Upset \n")

    print("5. Sleepy \n")

    print("6. Eating Food \n")

    print("7. Programming \n")

    print("8. In the Park \n")

    print("9. Playing PUBG \n")

    print("10. Overeaten? \n")

    print("11. Headache and Programming \n")

    print("12. Cooking \n")

    print("13. Talking to Phupo \n")

    print("14. Washing Dishes \n")

    print("15. Other \n")

    for i in range(1):

        choice = int(input("Select the mode to recognize your physical activity: \t"))

        if choice == 1:

            print(obj.activity2())

            break



        elif choice == 2 or choice == 5:

            print(obj.activity2())

            break



        elif choice == 3 or choice == 15:

            print(obj.activity4())

            break



        elif choice == 4 or choice == 15:

            print(obj.activity5())

            break



        elif choice == 10 or choice == 15:

            print(obj.activity3())

            break



        elif choice == 1 or choice == 13:

            print(obj.activity7())

            break



        elif choice == 11 or choice == 15:

            print(obj.activity2())

            break



        elif choice == 14 or choice == 15:

            print(obj.activity2())

            break



        elif choice == 8 or choice == 3:

            print(obj.activity4())

            break



        elif choice == 13 or choice == 15:

            print(obj.activity8())

            break



        elif choice == 13:

            print(obj.activity7())

            break



        else:

            print(obj.activity6())

            break