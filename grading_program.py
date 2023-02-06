#print the average marks for grading system
score_1 = int(input("please enter your first marks: "))
score_2 = int(input("please enter your second marks: "))
score_3 = int(input("please enter your third marks: "))

add = score_1 + score_2 + score_3
average = add/3

if (average >= 70 and average <= 100):
    print("you have scored an A")
if (average >= 60 and average <= 69):
    print("you have scored a B")
if (average >= 50 and average <= 59):
    print("you have scored a C")
if (average >= 40 and average <= 49):
    print("you have scored a D")
else: 
    print("You have failed")