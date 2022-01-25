
print ("shape sides to interior angels converter using the n(180-360/n) formula   ")
intro = '''

internal angle calculator v1.0.0 


                               /$$                  /$$$$$$  /$$                 /$$                                        /$$        /$$$$$$      /$$$$$$ 
                              | $$                 /$$__  $$|__/                | $$                                      /$$$$       /$$$_  $$    /$$$_  $$
  /$$$$$$  /$$$$$$$   /$$$$$$ | $$  /$$$$$$       | $$  \__/ /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$        /$$    /$$|_  $$      | $$$$\ $$   | $$$$\ $$
 |____  $$| $$__  $$ /$$__  $$| $$ /$$__  $$      | $$$$    | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$      |  $$  /$$/  | $$      | $$ $$ $$   | $$ $$ $$
  /$$$$$$$| $$  \ $$| $$  \ $$| $$| $$$$$$$$      | $$_/    | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/       \  $$/$$/   | $$      | $$\ $$$$   | $$\ $$$$
 /$$__  $$| $$  | $$| $$  | $$| $$| $$_____/      | $$      | $$| $$  | $$| $$  | $$| $$_____/| $$              \  $$$/    | $$      | $$ \ $$$   | $$ \ $$$
|  $$$$$$$| $$  | $$|  $$$$$$$| $$|  $$$$$$$      | $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$               \  $/    /$$$$$$ /$$|  $$$$$$//$$|  $$$$$$/
 \_______/|__/  |__/ \____  $$|__/ \_______/      |__/      |__/|__/  |__/ \_______/ \_______/|__/                \_/    |______/|__/ \______/|__/ \______/ 
                     /$$  \ $$                                                                                                                              
                    |  $$$$$$/                                                                                                                              
                     \______/                                                                                                                               



     Input a number to get started
1)   Input the number of sides you want to calculate
2)   Loop printing out numbers starting from 3
3)   Loop printing out numbers with keybord input reqired between outputs
4)   Loop output results to a new file (may rewrite existing data)
5)   Loop output results to a new file with keybord input reqired between outputs (may rewrite existing data)
6)   Loop output while resuming from previous file with keybord input required between outputs
7)   Loop output while resuming from previous file without keybord input reqired between outputs
8)   Display infomation about this program  '''

start_option = input(intro)

if start_option == "1":
    calculate = input ("how manny sides dose the shape have?   ")
    answer = int (calculate) * (180-360/int (calculate))
    print (answer)

elif start_option == "2":
    calculate = 3
    print ("press ctrl + c to stop at any time")
    input ("Press enter to start")
    while True:
        answer = int (calculate) * (180-360/(calculate))
        print (answer)
        calculate = calculate + 1

elif start_option == "3":
     calculate = 3
     while True:
        answer = calculate * (180-360/calculate)
        print (answer)
        calculate = calculate + 1   
        if input ("press enter to continue or type exit to stop   3") == "exit":
            break

elif start_option == "4":
    
    print ("press ctrl + c to stop at any time")
    input ("press enter to start")
    print ("writing to file ...")
    calculate = 3
    with open("output.txt", "w") as o:
        print ("clearing file")
    while True:
               
        with open("output.txt", "a") as o:
            answer =round (calculate * (180-360/calculate))
            o.write (str (calculate))
            o.write (" Sides = ")
            o.write(str(answer))
            o.write('\n')
            print (calculate)
            calculate = calculate + 1
    
elif start_option == "5":
    print ("press ctrl + c to stop at any time")
    input ("press enter to start")

    print ("writing to file ...")
    calculate = 3
    with open("output.txt", "w") as o:

        print ("clearing file")
    while True:
        if input ("press enter to continue Type exit to stop   ") == "exit":
            break
        
        with open("output.txt", "a") as o:
            answer = round (calculate * (180-360/calculate))
            o.write (str (calculate))
            o.write (" Sides = ")
            o.write(str(answer))
            o.write('\n')
            print (calculate)
            calculate = calculate + 1
        
        
elif start_option == "6":

    print ("checking for file")
    output = open("output.txt", "r")
    outputlist = output.readlines()
    output.close
    last_output = outputlist[len(outputlist)-1]
    print (last_output)
    input ("continue")
    calculate = int (last_output.split(" Sides = ")[0])

    print ("writing to file from previous...")

    while True:
        if input ("press enter to continue Type exit to stop   ") == "exit":
            break
        
        with open("output.txt", "a") as o:

            answer = round (calculate * (180-360/calculate))
            o.write (str (calculate))
            o.write (" Sides = ")
            o.write(str(answer))
            o.write('\n')
            print (calculate)
            calculate = calculate + 1

elif start_option == "7":

    print ("checking for file")
    output = open("output.txt", "r")
    outputlist = output.readlines()
    output.close
    last_output = outputlist[len(outputlist)-1]
    print (last_output)

    print ("press ctrl + c to stop at any time")
    input ("press enter to start")

    calculate = int (last_output.split(" Sides = ")[0])

    print ("writing to file from previous...")

    while True:

        with open("output.txt", "a") as o:

            answer = round (calculate * (180-360/calculate))
            o.write (str (calculate))
            o.write (" Sides = ")
            o.write(str(answer))
            o.write('\n')

            print (calculate)
            calculate = calculate + 1


elif start_option == "8":
    print ('''
    
    
                               /$$                  /$$$$$$  /$$                 /$$                                        /$$        /$$$$$$      /$$$$$$ 
                              | $$                 /$$__  $$|__/                | $$                                      /$$$$       /$$$_  $$    /$$$_  $$
  /$$$$$$  /$$$$$$$   /$$$$$$ | $$  /$$$$$$       | $$  \__/ /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$        /$$    /$$|_  $$      | $$$$\ $$   | $$$$\ $$
 |____  $$| $$__  $$ /$$__  $$| $$ /$$__  $$      | $$$$    | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$      |  $$  /$$/  | $$      | $$ $$ $$   | $$ $$ $$
  /$$$$$$$| $$  \ $$| $$  \ $$| $$| $$$$$$$$      | $$_/    | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/       \  $$/$$/   | $$      | $$\ $$$$   | $$\ $$$$
 /$$__  $$| $$  | $$| $$  | $$| $$| $$_____/      | $$      | $$| $$  | $$| $$  | $$| $$_____/| $$              \  $$$/    | $$      | $$ \ $$$   | $$ \ $$$
|  $$$$$$$| $$  | $$|  $$$$$$$| $$|  $$$$$$$      | $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$               \  $/    /$$$$$$ /$$|  $$$$$$//$$|  $$$$$$/
 \_______/|__/  |__/ \____  $$|__/ \_______/      |__/      |__/|__/  |__/ \_______/ \_______/|__/                \_/    |______/|__/ \______/|__/ \______/ 
                     /$$  \ $$                                                                                                                              
                    |  $$$$$$/                                                                                                                              
                     \______/                                                                                                                               

by KiwiHuman


This scrypt/program is a project I developed for fun after descovering a formula n(180-360/n) that calculates the sum of the internal angles in a polygon 
I do not expect this to be usefull for anything as regular shapes with absurd numbers of sides tend to look verry much like circles
and shapes with 100's of thousands of sides aren't often seen. However I thought this would be intersting to automate and got carried away with making a
full-blown scrypt to calculate and log the internal angles in shapes. I hope the scrypt could be intresting or usefull to someone but this was mainly an 
oppotunity to practice using python as I had not programmed in a while as well as learning to read and write files in python 

I would like to creddit w3schools.com/python for helping me with the many times I got stuck and had to google stuff this websid ewas very helpfull 
In the future I would like to make some improvements such as custom filenames and save locations as well as support for csv formats and maby more     ''')

    input ("press enter to end program")


