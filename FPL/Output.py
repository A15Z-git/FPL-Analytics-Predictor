from Base import name_list
from Base import Best11
from Base import ReturnWeeklyPts

print(""" 
    Hello! Welcome to the FPL score tracker and predictor!
    
    
    This project is still a work-in-progress! Please read documentation for functionality.
    
    These are the current functionalities available:
    
    1) Press 1 to Find the Best 11 scorers this season.
    2) Press 2 to see the Best 11 on a given week.
    3) Press 3 to end the program safely (or ig any other no. not mentioned).
    
    """)

User_choice = int(input("Please enter your choice: "))
while User_choice!=3:
    if User_choice == 1:
        print("The Best 11 are: ")
        for players in Best11:
           print(players[0], "with a total score of", players[1])

        print("")
        User_choice=int(input("Anything else you want to try? Please enter your choice: "))

    if User_choice==2:
        GW=int(input("Please enter your GW: "))
        if GW<1 or GW>38:
            print("Invalid GW. Why would you do this :(")
        else:
            print("In week", GW, "the top 11 players with their scores were:")
            BestWeekly11=ReturnWeeklyPts(GW)
            for players in BestWeekly11:
                print(players[0], players[1])

            User_choice=int(input("Anything else you want to try? Please enter your choice: "))
    if User_choice>3 or User_choice<1:
        break

