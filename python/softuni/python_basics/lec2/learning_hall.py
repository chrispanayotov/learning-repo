# Make a program that calculates the area of a rectangular hall
# Calculate the amount of work spaces in it

h = float(input()) * 100 # Converting to cm
w = float(input()) * 100 # Converting to cm

# Calculatng the amount of workspaces in the width
total_width = int(w) - 100 # width of hall minus corridor
workspace_w = 70 # width of a workspace in cm
amount_workspace_w = int(total_width / workspace_w)

# Calculating the amount of workspaces in the height
total_height = int(h)
workspace_h = 120 # height of a work space in cm
amount_workspace_h = int(total_height / workspace_h)

total_workspaces = amount_workspace_w * amount_workspace_h - 3
print(total_workspaces)