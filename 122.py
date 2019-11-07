# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rdm
import leaderboard as lb

#--------------------leaderboard variables-------------------------
leaderboard_file_name = "a112_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter youre name.")



#-----game configuration----
shape = "turtle"
size = 5
color= "green"
score = 0
points = 0
font_setup = ("Arial", 20, "bold")
timer = 15
counter_interval = 1000   #1000 represents 1 second
timer_up = False
counter =  trtl.Turtle()
counter.penup()
counter.goto(325, 320)
counter.pendown()
counter.ht()
#-----initialize turtle-----shape = shape
count = 0



t = trtl.Turtle(shape = shape)
t.shapesize(size)
t.color(color)
t.speed(0)
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-450, 320)
font = ("Arial", 50, "bold")
score_writer.write(score, font = font)
score_writer.ht()
#-----game functions--------
def turtle_clicked(x,y):
    print("Squidward was clicked")
    change_position()
    score_counter()
    score_writer.clear()
    score_writer.write(score, font = font)
def change_position():
    t.penup()
    t.ht()
    new_xpos = rdm.randint(-400,400)
    new_ypos = rdm.randint(-300,300)
    t.goto(new_xpos, new_ypos)
    t.st()
    new_size = rdm.randint(2,6)#customazation - random size
    t.shapesize(new_size)#customazation - random size
def score_counter():
    global score


        
    score += 1
    print(score)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    counter.penup()
    timer_up = True
    game_over()
    manage_leaderboard()
    

  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
def game_over():
    t.ht()
    t.penup()
    t.goto(100000000000000000000000000000000000000, 1000000000000000000000000000000000000000000)
    wn.bgcolor("red") #customization - chages backround color to black at end of game
    counter.goto(0, 200)#customazation - uses score writer to write score in middle of screen
    counter.color("white")#customazation - uses score writer to write score in middle of screen
    counter.pendown()
    counter.write(score, font = font)#customazation - uses score writer to write score in middle of screen
    counter.penup()
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  counter.pendown()
  
  global leader_scores_list
  global leader_names_list
  global score
  global t

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

# TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, t, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, t, score)



#-----events----------------
t.onclick(turtle_clicked)





wn = trtl.Screen()
wn.bgcolor("lightblue")#customazation - background color
wn.ontimer(countdown, counter_interval) 
wn.mainloop()