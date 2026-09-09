# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Reading Multi Line Input
#  Author       : Team Tinitiate
# ==============================================================================



l_UserInput = ""
terminate_str = ":END"  # Termination String ':END'

print("Enter multiline user input, Please enter the string ':END'")
print("to terminate reading input")
while True:
    data = input()
    if data.strip() == terminate_str:
        break
    l_UserInput += "%s\n" % data

print(l_UserInput)
