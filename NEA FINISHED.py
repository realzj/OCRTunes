import csv

def validate(string, chars):
    return True in [c in string for c in chars]

def contains(string, chars):
    return True in [c in string for c in chars]

sign_up = " "
while sign_up!= "Y" and sign_up!= "N":
    sign_up = input("Do you want to create an account? Y/N: ").upper()
    while sign_up == "N":
        if sign_up == "N":
            print("You have to create an account to access OCRtunes")
            sign_up = input("Do you want to create an account? Y/N: ").upper()


if sign_up == "Y":
    
    name = ""
    while name == "":
        name = input("What is your name? ")
        
    DoB = ""
    print("Dont leave any space between day, month and year")
    while DoB.isnumeric() == False:
        DoB = input("What is your Date of Birth? ")

    Favourite_artist = ""
    while Favourite_artist  == "":
        Favourite_artist = input("Who is your favourite artist? ")

    Favourite_genre = ""
    while Favourite_genre  == "":
        Favourite_genre = input("What is your favourite genre of music? ")


    Username = ""
    while Username == "":
        Username = input("Create a username: ")


    Password = ""
    while len(Password) <8 or len(Password)>16:
        Password = input("Create a password: ")
        
        f = open("userinfo.txt","w")
        f.write("User information"+"\n")
        f.write(str(name)+"\n")
        f.write(str(DoB)+"\n")
        f.write(str(Favourite_artist)+"\n")
        f.write(str(Favourite_genre)+"\n")
        f.write(str(Username)+"\n")
        f.write(str(Password)+"\n")
        f.close()

else:
    print()


def library():
        info = []
        file = open("info.csv","r")
        data = csv.reader(file)
        for row in data:
            print(row)
        Menu()
def Details():
        info = []
        txt = open("userinfo.txt","r")
        data = txt.readlines()
        for row in data:
            print(row)
        Menu()

def Alpha():

    A = []
    fileA = open("info.csv","r")
    data = csv.reader(fileA)
    for row in data:
        A.append(row[0])
    A.sort()
    print("This are the songs: ")
    print("\n")
    i=0
    while (i<len(A)):
           print(A[i])
           i = i+1
    Menu()
    

    
        
def New():
    print("\n")
    Favourite_genre = ""
    while Favourite_genre  == "":
        Favourite_genre = input("What is your favourite genre of music? ")

        f = open("userinfo.txt","w")
        f.write("User information"+"\n")
        f.write(str(name)+"\n")
        f.write(str(DoB)+"\n")
        f.write(str(Favourite_artist)+"\n")
        f.write(str(Favourite_genre)+"\n")
        f.write(str(Username)+"\n")
        f.write(str(Password)+"\n")
        f.write("New Genre:"+"\n")
        f.write(str(Favourite_genre)+"\n")
        f.close()
        Menu()
            
def New2():
    print("\n")
    Favourite_artist = ""
    while Favourite_artist  == "":
        Favourite_artist = input("Who is your favourite artist? ")

        f = open("userinfo.txt","w")
        f.write("User information"+"\n")
        f.write(str(name)+"\n")
        f.write(str(DoB)+"\n")
        f.write(str(Favourite_artist)+"\n")
        f.write(str(Favourite_genre)+"\n")
        f.write(str(Username)+"\n")
        f.write(str(Password)+"\n")
        f.write("New favourite artist"+"\n")
        f.write(str(Favourite_artist)+"\n")
        f.close()
        Menu()

def Files():
        print("4.Genre")
        print("5.Artist")
        valid = False
        while not valid:
            choice2 = input("Enter your choice: ")
            if not validate(choice2,"45"):
                print("Invalid option")
            else:
                valid = True
    
        if choice2 == "4":
            print("6.Pop")
            print("7.Trap")
            print("8.Reguetton")
            valid = False
            while not valid:
                choice3 = input("Enter your choice: ")
                if not validate(choice3,"678"):
                    print("Invalid option")
                else:
                    valid = True
            
            if choice3 == "6":
                pop = []
                file2 = open("pop.csv","r")
                data = csv.reader(file2)
                for row in data:
                    print(row)
                Menu()

                
            elif choice3 == "7":
                trap = []
                file3 = open("trap.csv","r")
                data = csv.reader(file3)
                for row in data:
                    print(row)
                Menu()
                
            elif choice3 == "8":
                trap = []
                file4 = open("reguetton.csv","r")
                data = csv.reader(file4)
                for row in data:
                    print(row)
                Menu()
                
        elif choice2 == "5":
            print("M.Michael Jackson")
            print("U.Bad Bunny")
            print("E.Daddy Yankee")
            print("O.Farruko")
            print("A.Anuel AA")
            valid = False
            while not valid:
                choice4 = input("Enter your choice: ")
                if not validate(choice4,"MmUuEeOoAa"):
                    print("Invalid option")
                else:
                    valid = True
            
            if choice4 == "M":
                mj = []
                file5 = open("mj.csv","r")
                data = csv.reader(file5)
                for row in data:
                    print(row)
                Menu()
            elif choice4 == "m":
                mj = []
                file5 = open("mj.csv","r")
                data = csv.reader(file5)
                for row in data:
                    print(row)
                Menu()

            elif choice4 == "U":
                bb = []
                file6 = open("bb.csv","r")
                data = csv.reader(file6)
                for row in data:
                    print(row)
                Menu()

            elif choice4 == "u":
                bb = []
                file6 = open("bb.csv","r")
                data = csv.reader(file6)
                for row in data:
                    print(row)
                Menu()
                    
            elif choice4 == "E":
                dy = []
                file7 = open("dy.csv","r")
                data = csv.reader(file7)
                for row in data:
                    print(row)
                Menu()

            elif choice4 == "e":
                dy = []
                file7 = open("dy.csv","r")
                data = csv.reader(file7)
                for row in data:
                    print(row)
                Menu()

            elif choice4 == "O":
                F = []
                file8 = open("Farruko.csv","r")
                data = csv.reader(file8)
                for row in data:
                    print (row)
                Menu()

            elif choice4 == "o":
                F = []
                file8 = open("Farruko.csv","r")
                data = csv.reader(file8)
                for row in data:
                    print (row)
                Menu()

                    
            elif choice4 == "A":
                AA = []
                file9 = open("AA.csv","r")
                data = csv.reader(file9)
                for row in data:
                    print(row)
                Menu()
                
            elif choice4 == "a":
                AA = []
                file9 = open("AA.csv","r")
                data = csv.reader(file9)
                for row in data:
                    print(row)
                Menu()

def Create():
    #CREATES A FILE WITH ALL THE SONGS THAT ARE THE GENRE OF POP
    option = "Pop"
    data = list(csv.reader(open("info.csv")))

    playlist = open("playlist.csv","a+")#CREATES NEW FILE

    for i in range(len(data)):
        if data [i][2] == option:#SEARCHS THW WHOLE ROW OF 3 FOR THE "POP"
            playlist.write(str(data[i]))#ADDS THE SONGS FROM POP TO THE NEW FILE THAT WAS CREATED CALLED PLAYLIST
            playlist.write(str("\n"))#LEAVES A LINE BETWEEN THEM
    print("New Playlist successfully created")
    playlist.close()#CLOSES THE PLAYLIST
    Menu()    
def Create2():
    #CREATES A FILE WITH ALL THE SONGS THAT ARE THE GENRE OF TRAP
    option = "Trap"
    data = list(csv.reader(open("info.csv")))

    playlist1 = open("playlist1.csv","a+")

    for i in range(len(data)):
        if data [i][2] == option:
            playlist1.write(str(data[i]))
            playlist1.write(str("\n"))
    print("New Playlist successfully created")
    playlist1.close()
    
    Menu()
    
def Create3():
    #CREATES A FILE WITH ALL THE SONGS THAT ARE THE GENRE OF REGUETTON
     option = "Reguetton"
     data = list(csv.reader(open("info.csv")))

     playlist2 = open("playlist2.csv","a+")#CREATES A NEW FILE

     for i in range(len(data)):
         if data [i][2] == option:#SEARCHS THW WHOLE ROW OF 3 FOR THE "REGUETTON"
             playlist2.write(str(data[i]))#ADDS THE SONGS FROM POP TO THE NEW FILE THAT WAS CREATED CALLED PLAYLIST2
             playlist2.write(str("\n"))#LEAVES A LINE BETWEEN THEM
     print("New Playlist successfully created")
     playlist2.close()
     Menu()

def Create4():
    #THIS IS THE CODE TO CREATE THE PLAYLIST OF THE USERS INPUT LENGTH
    time_limit = int(input("Choose the length you want the playlist to be in: "))
    
    data = list(csv.reader(open("info.csv")))
    playlist3 = open("playlist3.csv","a+")
    total = 0
    
    for i in range(len(data)):
        total = total + int(data[i][3])
        if total <= time_limit:#COMPARES IF THE USERS INPUT IS LESS THAN OR EQUAL TO THE TOTAL WHICH
            playlist3.write(str(data[i]))
            playlist3.write(str("\n"))#LEAVES A LINE BETWEEN THEM
        else:
            break#END THE LOOP ONCE IT FINISHES TO REACH THE USERS INPUT
            
    print("New Playlist successfully created")
    playlist3.close()
    Menu()

def Create5():
    
    artist = "Michael Jackson"
    data = list(csv.reader(open("info.csv")))
    
    playlist4 = open("playlist4.csv","a+")#CREATES A NEW FILE
    
    for i in range(len(data)):
        if data [i][1] == artist:#SEARCHS THE WHOLE ROW OF 3 FOR THE NAME OF "MICHAEL JACKSON"
            playlist4.write(str(data[i]))#ADDS THE SONGS FROM MICHAEL JACKSON TO THE NEW FILE THAT WAS CREATED CALLED PLAYLIST2
            playlist4.write(str("\n"))#LEAVES A LINE BETWEEN THEM

    print("New Playlist successfully created")
    playlist4.close()
    Menu()

def Create6():

    artist = "Bad Bunny"
    data = list(csv.reader(open("info.csv")))

    playlist5 = open("playlist5.csv","a+")#CREATES A NEW FILE

    for i in range(len(data)):
        if data [i][1] == artist:
            playlist5.write(str(data[i]))
            playlist5.write(str("\n"))

    print("New Playlist successfully created")
    playlist5.close()
    Menu()

def Create7():

    artist = "Daddy Yankee"
    data = list(csv.reader(open("info.csv")))

    playlist6 = open("playlist6.csv","a+")#CREATES A NEW FILE

    for i in range(len(data)):
        if data [i][1] == artist:
            playlist6.write(str(data[i]))
            playlist6.write(str("\n"))
    print("New Playlist successfully created")
    playlist6.close()
    Menu()

def Create8():

    artist = "Farruko"
    data = list(csv.reader(open("info.csv")))

    playlist7 = open("playlist7.csv","a+")#CREATES A NEW FILE

    for i in range(len(data)):
        if data [i][1] == artist:
            playlist7.write(str(data[i]))
            playlist7.write(str("\n"))
    print("New Playlist successfully created")
    playlist7.close()
    Menu()

def Create9():

    artist = "Anuel AA"
    data = list(csv.reader(open("info.csv")))

    playlist8 = open("playlist8.csv","a+")#CREATES A NEW FILE

    for i in range(len(data)):
        if data [i][1] == artist:
            playlist8.write(str(data[i]))
            playlist8.write(str("\n"))
    print("New Playlist successfully created")
    playlist8.close()
    Menu()


def Playlist():
    print("P.POP")
    print("\n")
    print("T.TRAP")
    print("\n")
    print("R.REGUEGETTON")
    print("\n")
    print("L.LENGTH")
    print("\n")

    valid = False
    while not valid:
        option = input("Choose an option: ")
        if not validate(option,"PpTtRrLl"):#ONLY ALLOWS THIS CHARACTERS TO BE CHOSEN
            print("Invalid option")
        else:
            valid = True

    if option == "P":
        Create()
    if option == "p":
        Create()
    if option == "T":
        Create2()
    if option == "t":
        Create2()
    if option == "R":
        Create3()
    if option == "r":
        Create3()
    if option == "L":
        Create4()
    if option == "l":
        Create4()

    
        
def Artist():
    print("M.Michael Jackson")
    print("B.Bad Bunny")
    print("D.Daddy Yankee")
    print("F.Farruko")
    print("A.Anuel AA")
    valid = False
    while not valid:
        artist = input("Enter an option: ")
        if not validate(artist,"MmBbDdFfAa"):
            print("Invalid option")
        else:
            valid = True

    if artist == "M":
        Create5()
    if artist == "m":
        Create5()
    if artist == "B":
        Create6()
    if artist == "b":
        Create6()
    if artist == "D":
        Create7()
    if artist == "d":
        Create7()
    if artist == "F":
        Create8()
    if artist == "f":
        Create8()
    if artist == "A":
        Create9()
    if artist == "a":
        Create9()
    
    
        
def Menu(): #This is the menu will always have access
    print ("\n")
    print ("1.View all the songs in the library. ")
    print ("\n")
    print ("S.View all the songs in the library by alphabetical order. ")
    print ("\n")
    print ("2.Look at your personal details ")
    print ("\n")
    print ("A.Change your Favourite Genre")
    print ("\n")
    print ("B.Change your Favourite Artist")
    print ("\n")
    print ("3.Genres, artist in library. ")
    print ("\n")
    print ("4.Creates a playlist of your choice. ")
    print ("\n")
    print ("5.Creates a playlist from an artist name.")
    print ("\n")
    print ("6.Exit the program")
    print ("\n")
    valid = False
    while not valid:
        choice = input("Enter an option: ")
        if not validate(choice,"123456ABabSs"):
            print("Invalid option")
        else:
            valid = True
    
    if choice == "1": #From this line to line 368 are all the options the user can input when the user inputs one it will take them to their input
        library()#SHOW ALL THE SONGS IN THE LIBRARY
    if choice == "2":
        Details()#SHOW USERS DETAILS
    if choice == "A":
        New()#ALLOWS THE USER TO CHANGE THEIR FAVOURITE GENRE
    if choice == "a":
        New()
    if choice == "B":
        New2()#ALLOWS THE USER TO CHANGE THEIR FAVOURITE ARTIST
    if choice == "b":
        New2()
    if choice == "3":
        Files()#WILL ALLOW THE USER TO SHOW ALL THE FILES FROM ARTISTS AND GENRES
    if choice == "4":
        Playlist()
    if choice == "S":
        Alpha()#WILL ALLOW THE USER TO VIEW THE LIBRARY IN ALPHABETICAL ORDER
    if choice == "s":
        Alpha()
    if choice == "5":
        Artist()
    if choice == "6":
        exit()
Menu()

