#-----score config-----
from os import close


bronze_score = 15
silver_score = 20
gold_score = 25

#load leaderboard from file
def load_leaderboard(file_name, leader_names, leader_scores):

	leaderboard_file = open(file_name, "r")

	#using for loop to iterate through the content of the file, one line at a time
	for line in leaderboard_file:
		leader_name = ""
		leader_score = ""
		index = 0

		# TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")
		while (line[index] != ","):
			leader_name = leader_name + line [index]
			index = index + 1
		# the loop ends when index is pointing at the comma character
		print("leader name is:", leader_name)

		# TODO 2: add the leader name to the list

		leader_names.append(leader_name)

		# TODO 3: read the player score using a similar loop

		index = index + 1
		while (line[index] != "/n"):
			leader_score = leader_score + line[index]
			index = index + 1

		


	leaderboard_file.close()

	#update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):

	leader_index = 0

	#store the latest leaderboard back in the file
	leaderboard_file = open(file_name, "w") #this mode opens the file and erases its contents for a fresh start
	leader_index = 0

	leaderboard_file.close()

#draw leaderboard and display message to player.
def draw_leaderboard(leader_names, leader_scores, high_scorer, turtle_object, player_score):

	#clear the screen and move the writer to (-200, 100) to start drawing the leaderboard
	font_setup = ("Arial", 20, "normal")
	turtle_object.clear()
	turtle_object.penup()
	turtle_object.setposition(-200,100)
	turtle_object.hideturtle()
	turtle_object.pendown()

	leader_index = 0

	#loop through the lists and use the same index to display the corresponding name and score, seperatred by a tab space '/t'


