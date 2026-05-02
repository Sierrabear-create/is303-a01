'''
Sierra Andreason 
IS 303 - A01

Paint Estimate Calculator
This calculator estimates how many gallons 
of paint are needed to paint a room.

Inputs: 
- Room Name (string)
- Wall Height (ft--)
- Total Wall Width (ft--)

Processes: 
-Multiple total Square feet needed to cover
-Divide total by 350 to find the number of needed gallons

- Gallons needed = (Height * Width)/350 (feet squared)
- One Gallon covers ~350 feet squared (INTEGER)

Outputs:
- Print the Gallons needed and the Room Name 
  in a formatted message

'''
#INPUTS
room_name = input("What is the Room's Name? ")
wall_height = int(input("What is the Height of the Wall? "))
wall_width = int(input("What is the Width of the Wall? "))

#PROCESSES
gallons_needed = (wall_height * wall_width)/350

#OUTPUTS
print ("---")
print(f"{room_name} ~ {gallons_needed} Gallons Needed")
