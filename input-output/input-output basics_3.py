name = input("enter name")
roll_no =input("enter roll no")
age = input ("enter age")
science_marks =int(input("marks in science"))
math_marks =int(input("marks in math"))
chemistry_marks =int(input("marks in chemistry"))



total_marks = science_marks+math_marks+chemistry_marks
average = (total_marks)/3

print("Name:",name,"Roll_no:",roll_no,"Age:",age,"Total_marks:",total_marks,"Average:",average,sep="\n")