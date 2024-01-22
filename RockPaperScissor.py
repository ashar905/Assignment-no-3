import random

print("1 for rock","\n2 for paper","\n3 for scissor")
userinput = int(input("enter your choice"))
userchoice = ""
option = ["rock","paper","scissor"]
computerchoice = random.choice(option)


if userinput == 1 :
    userchoice = "rock"
elif userinput == 2 :
     userchoice = "paper"
elif userinput == 3 :
     userchoice = "scissor"
else :
     print("Please enter a valid number!")
print("computer choice =",computerchoice)     
print("user choice =",userchoice)

if computerchoice == userchoice :
     print("draw")
else :
     if computerchoice == "rock" and userchoice == "paper" :
          print("user win , paper beat rock")
     elif computerchoice == "rock" and userchoice == "scissor" :
          print("computer win , rock beat scissor")
     elif computerchoice == "paper" and userchoice == "rock" :
          print("computer win , paper beat rock")
     elif computerchoice == "paper" and userchoice == "scissor" :
          print("user win , scissor beat paper")
     elif computerchoice == "scissor" and userchoice == "paper" :
          print("computer win , scissor beat paper")
     elif computerchoice == "scissor" and userchoice == "rock" :
          print("user win , rock beat scissor")                    
                    
               