# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

print(student_heights)
sum = 0
step = 0

for i in student_heights:
  sum = sum + i
  step += 1

average = round(sum/step)
print(f"Avarage student height is {average}")
#value_1 = student_heights[0]
#print(value_1)


