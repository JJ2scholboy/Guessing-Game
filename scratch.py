# guessing game
import random
user_wins = False
score = 0
user_ends = False

def raten():
    #score = 0
    #print(f"Du hast {score} mal geraten")
    user_wins = False
    score = 0
    while not user_wins:
        try:
            guess = int(input("Geben Sie eine Zahl zwischen 1 und 100 ein: "))
            if guess < 0 or guess > 100:
                raise ValueError
        except:
            print("Falsche eingabe.")
            continue

        # wenn kein fehler aufgritt.

        score = score +1
        if number == guess:
            print(f"Yes, {number} is winner")
            user_wins = True
            print("Dein score ist", score)
            #raten()

        elif guess > number:
            print("Die gesuchte Zahl ist kleiner")

        else:
            print("Die gesuchte Zahl ist größer")
        #else:
         #   continue

#try:
while not user_ends: #while not user_wins:   #while(solange) Bedingung:     not b / b = False ist das gleiche
    number = random.randint(1, 100)
    print(f"DEBUG: Number ist {number}")
    user_wins = False
    raten()
    try:
        neustart = (input("Möchte Sie erneut spielen: ja oder nein "))
    except:
        print("Falsche eingabe. Nur (ja) oder (nein) ")
        continue
    if neustart == "nein":
        user_ends = True

        #continue springt zur letzten while schleife/ break springt aus der while schleife raus


#except:
    #continue
#    print("Falsche Eingabe")

    #finally

#if guess ≠ type(int)
#continue




#    try:
 #           while not user_wins:
#
 #           #guess = int(input("Geben Sie eine Zahl zwischen 1 und 100 ein: "))
#
#
 #           #score = score +1
  #          if number == guess:
   #             print(f"Yes, {number} is winner")
    #            user_wins = True
#                print("Dein score ist", score)
 #               #raten()
#
 #           elif guess > number:
  #              print("Die gesuchte Zahl ist kleiner")
#
 #           else:
  #              print("Die gesuchte Zahl ist größer")
   # except:

    #user_plays = True
    #number = random.randint(1, 100)
   # print(f"DEBUG: Number ist {number}")
    #guess = int(input("Geben Sie eine Zahl zwischen 1 und 100 ein: "))
    #user_plays = True
# try:
#     except:
#     continue
 #except:
         #   print("falsche Eingabe")
          #  continue
# spiel neustart durch funktion oder zweite while schleife

#def raten():
 #   print("Du hast oft geraten")
