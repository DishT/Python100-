x = 0
y = 0

while True:
	s = input("Enter your steps: ")
	if not s:
		break
	action = s.split()[0]
	action_number = int(s.split()[1])
	if action == "UP":
		y += action_number
	elif action == "DOWN":
		y -= action_number
	elif action == "LEFT":
		x -= action_number
	elif action == "RIGHT":
		x += action_number


distance = int((x**2 + y**2)**0.5)

print (distance)