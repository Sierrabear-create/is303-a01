'''
Sierra Andreason 
IS 303 - A01

XP Calculator
This calculator estimates how many gaming sessions are needed
to reach your target level.

Inputs: 
- Player Name (string)
- Current XP (integer)
- Target XP (integer)
-XP earned per session (float)

Processes: 
-Subtract target xp from current xp 
-Then divide by xp needed per session to find number of sessions needed

Outputs:
- Print the Player's Name, Current XP, Target XP, and Session XP
  in a formatted message

'''
#INPUTS
player_name = input("What is the Gamer's Name? ")
current_xp = int(input("What is your Current XP? "))
target_xp = int(input("What is your Target XP? "))
session_xp =float(input("How much XP is needed per session? ")) 
#is the xp per session hard-coded?

#PROCESSES
sessions_needed = (target_xp-current_xp)/session_xp

#OUTPUTS
print ("---")
print(f"Player's Name: {player_name} ~ Current XP: {current_xp}")
print(f"Target XP: {target_xp} ~ Sessions Needed: {sessions_needed}")
