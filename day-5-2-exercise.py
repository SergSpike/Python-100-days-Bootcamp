# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

i = 0



for highest_score in student_scores:
  #print(highest_score)
  if highest_score > i:
    i = highest_score
print(f"The highest score in the class is: {i}")


