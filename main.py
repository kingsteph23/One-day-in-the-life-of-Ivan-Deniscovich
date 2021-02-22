intro = input("  _______________________ "
              "\n|  One day in the life | "
              "\n|     of               |   "
              "\n|   Ivan Denisovich    |  "
              "\n|                      |  "
              "\n|     start            |   "
              "\n|     quit             |  "
              "\n|______________________|"
              "\n>>")
print()
if intro == "quit":
    print("Hmmm, no way Comrade. Because of your crimes against the state,"
          "\nI will not allow it")
else:
    print("Lets us begin comrade Shukhov.")
print()
# Name of character from the book/Who you're playing as
comrade = "Ivan Denisovich Shukhov "
# Reason why you're in the Gulag
input("Early 1950s-Soviet Union"
      "\nYour name is " + comrade + "."
    "\nDue to accusations of being a spy working for the Germans during the Great Patriotic War,"
    "\nYou have been sentenced to ten years of hard labor."
     "\nYou will now be moved into a labor camp in Siberia known as 'Camp HQ' ")

print()
# Actual start of the game
input("Winter- Camp HQ- Siberia,USSR"
      "\n1951"
      "\nPrisoner Shcha-854"
      "\n" + comrade + " ")
print()
# Options of sleeping  in or reporting to your team. Results
rollcall = input("You wake up one morning, regular day,"
                 "\nThe Zeks(Camp inmates) are preparing for labor, same with your own team, Gang 104."
                 "\nHowever, you wake up to a fever and severe aches in your body...."
                 "\nDO YOU..."
                 "\n(Sleep)Sleep in"
                 "\n(Report)Report to your team"
                 "\n>>")
print()
if rollcall == "Sleep in" or rollcall == "Sleep":
    print("You wake up, and realize it is time for breakfast."
          "\nYou see two other inmates,Buynovsky(Known as the baptist) and Alyoshka, who is  praying."
          "\nHowever, due to you deciding to sleep in, "
          "\nthe new warden decides that you will be sentenced to three days in the hole.😱😱")

elif rollcall == "Report to your team" or "Report":
    print("You attempt to get out of bed, bu, you fall right back to sleep😴😴"
          "\nYou wake up and realize its breakfast time."
          "\nAt the same time, due to oversleeping,"
          "\nthe new warden decides that you will be sentenced to three days in the hole😱😱")
    print()
input("However, you get lucky Comrade Shukhov, because today your task is washing the floors"
      "\nof the Warden Quarters!!!"
      "\nNow get to washing comrade")
print()
input("But in all seriousness, if you pull something like that, you will seriously spend three days in the hole.")
print()
# Washing the headquarters
headquarters = input("Now, inside the wardens quarters, you are required to clean the floor."
                     "\nBut up to what quality do you clean the floor? 🤔"
                     "\nDo the job quickly"
                     "\nActually clean it"
                     "\n>>")
if headquarters == "Do the job quickly" or "Actually clean it":
    print("Who cares, as long as the floor looks good."
          "\nWho care about the actually quality?!")

print()
input("🔔🔔TIME FOR BREAKFAST🔔🔔. REPORT TO THE MESS HALL")
print()
messhall = input("You arrive at the mess hall, you behold, YOU get to select what you eat today"
                 "\nSelect a meal:"
                 "\nBread"
                 "\nMeat"
                 "\nSoup"
                 "\n>>")
# choice of foods(cant choose any because this is the USSR ;)
if messhall == "Bread" or messhall == "Meat" or messhall == "Soup":
    print("Funny, but no."
          "\nYou really thought you get to choose what YOU wanted to eat?"
          "\nEspecially out of all places, a gulag in the middle of Siberia, in the Soviet Union?"

          "\nPlus, why would we give any of these things to a spy?"
          "\nToo funny")
print()
input("But, we'll give you leftovers of fish and some gruel. maybe if you came earlier,"
      "\nMaybe you would've got more than just leftovers.")
print()
input("You finish your meal, but decide to go to the medical clinic due to the fact you weren't"
      "\nfeeling so well earlier in the day."
      "\nUnfournatly, the clinic is closed, and the medical orderly tells you you should've came the previous night.")
print()
input("BUT, medical orderly Kolya Vdovushkin does agree to take your temperature...")
print()
input("After a quick temperature check,your temperature is...."
      "\nTemperature:99 degrees Fahrenheit(37.2 degrees celsius)"
      "\nUnfortunately,This is considered to be slightly too low as a excuse for a days work. ")
print()
clinic = input("However, Medical Orderly does give you the  option  to linger in the clinic for a bit,"
               "\nBut is very risky, and result in your punishment."
               "\nOr just return to work."
               "\nWhich would you do?"
               "\n(Return)Return to work"
               "\n(Stay)Stay in the Clinic"
               "\n>>")
if clinic == "Stay in the Clinic" or clinic == "Stay":
    print("For some time, you stay in the clinic,"
          "\nHowever, the warden officer who gave you the warning earlier,"
          "\nenters the clinic."
          "\nAnd you get the special prize of being sentenced to three days in the hole"
          "\n3,653 days to go!")
    exit()
elif clinic == "Return to work" or clinic == "Return":
    print("Smart choice because it was either that or the hole."
          "\nYou decide to go back to the hut of your team, Gang 104, where Pavlo greets you. ")
print()
input("Eventually, you and your team(Gang 104, is called up for 'The Search'......")
print()
# The search.  Inspection in the middle of winter in siberia
thesearch = input("The disciplinary officer Volkovoy orders the prisoner to unbutton their shirts for body search."
                  "\nDespite the fact you have nothing to hide..."
                  "\nDo you....."
                  "\n(Submit)Submit to the search"
                  "\nor"
                  "\n(Resist)Resist the Search"
                  "\n>>")
if thesearch == "Resist" or thesearch == "Resist the Search":
    print("Disciplinary officer Volkovoy gets his braided leather lash, and whips you for falling out of line"
          "\nAfter this, you silently wipe the blood from your neck and go about your day.")
else:
    print("The only thing you have is regulation clothing and human chest with a soul inside it. "
          "\nBut hey at least you didn't end up like Buynovsky who just made a fuss,"
          "\nand got his butt whopped by the disciplinary officer😉"
          "\nGood thinking Comrade😉")

print()
input("Guards-EVERYONE LINE UP,ITS TIME TO GO TO THE POWER STATION!")
print()
input("You and your team is required to go work at the power station."
      "\nThe gang members are lined up in groups of 5, counted, and recounted,"
      "\nAnd are forced to do this march in the biting wind ")
print()
# March to the power station. Choices whether to get out of line, or stay in line
march = input("You and your team begin your march to the power station,"
              "\nHowever, you realized that you need to tie your shoes."
              "\nDo you..."
              "\n(Step out) Step out of line and tie your shoes"
              "\nor"
              "\n(Continue)Just continue the march and not even worry")
if march == "Step out of line and tie your shoes" or march == "Step out":
    input("🔫"
          "\nWithout the a second, the guards proceed to sho..."
          "\nOkay they didn't shoot you, its too cold too even talk in Siberia,"
          "\nSo, you just end up tucking your laces in. ")
else:
    print('Good choice.  But while marching,'
          '\nYou also realize the job of a guard isn''t that easy as well.')
print()
input("You arrive the Power station worksite,"
      "\nbut you also see the strong but kind foreman Tyurin for your first camp which was at Ust-Izhma"
      "\nThe task for today is walling in the second floor of the power station:")
print()
input("You and gang 104 work away, whether its sending a teenager to fetch wire for the pipes,"
      "\nand end up teaching him how to do a spoon, you continue working until you hear"
      "\nthat it is time for the noon meal")
print()
highnoon = input("Since its noon,"
                 "\nYou and your team decide to rest,"
                 "\nHowever it is too soon to start laying bricks"
                 "\nDo you....."
                 "\n(eat)Just  eat your meal"
                 "\nor"
                 "\n(lay) Lay the bricks"
                 "\n>>")

if highnoon == "Lay the bricks" or highnoon == "lay":
    print("Since you decided to do Comrade, the mortar is starting to dry up in the trough")
    breakpoint()
else:
    weneedfood = input("Since it is now lunch,"
                       "\nYOU get to choose what you want to eat"
                       "\nSelect a Meal of your choice Comrade Shukov:"
                       "\nGruel"
                       "\nGruel"
                       "\nGruel"
                       "\nor"
                       "\nGruel"
                       "\n>>")
if weneedfood == "Gruel":
    print("Ah yes, the wonderful meal of Oatmeal Gruel,"
          "\nI hope you weren't to expecting to get some luxury like meat or bread,"
          "\nOther than that, here's a extra  meal of Oatmeal Gruel for you Comrade!")

print()
input("you end up getting more rations for your fellow comrades since you did one of the following:"
      "\nCarrying bags of a meal, collecting dirty bowls, or any task a cook is supposed to do. "
      "\nComrade Pavlo, Comrade Gopchick also gets their rations. Although, the foreman receives a double ration.")
print()
input("BREAK TIME IS OVER, BACK TO WORK COMRADES"
      "\nYou arrive back at the")
