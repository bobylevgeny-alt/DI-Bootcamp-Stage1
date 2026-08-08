# number_of_user = int(input("Number of user:"))
# user_list = list(range(1, number_of_user +1))
# number_of_teams = number_of_user // 3
# list_of_teams = []
# print(number_of_teams)
# for number in range(1, 3 * number_of_teams, 3):
#     team = tuple(user_list[number - 1: number + 2])
#     list_of_teams.append(team)
# print(list_of_teams)
    
# # # Description 

# a = {
#     "fruit": ["apple", "banana", "orange"],
#     "baked_goods": ["bread", "cake", "cookies"]}

# a = {
#     "name": ["John", "Jane", "Bob"],
#     "last_name": ["Doe", "Smith", "Johnson"],
#     "age": [25, 30, 35],
#     "program": ["Computer Science", "Mathematics", "Physics"],
#     "courses": ["Math 101", "CS 201", "PH 301"]
# }

# students = []

# for i in range(len(a["name"])):
#     student = {
#         "name": a["name"][i],
#         "last_name": a["last_name"][i],
#         "age": a["age"][i],
#         "program": a["program"][i],
#         "course": a["courses"][i]
#     }

#     students.append(student)

# print(students)  

# a = {
#     "name": ["John", "Jane", "Bob"],
#     "last_name": ["Doe", "Smith", "Johnson"],
#     "age": [25, 30, 35],
#     "program": ["Computer Science", "Mathematics", "Physics"],
#     "courses": ["Math 101", "CS 201", "PH 301"]
# }

# a["name"] = "Mike"
# a["age"] = 40
# a["height"] = 180

# print(a.items())
# print(a.keys())
# print(a.values())

# print("height" in a)
# del a["height"]
# print("height" in a)

# for k in a:
#     print(a[k])  
#     print(f"The key is: {k} and the value is: {a[k]}")

# for num in range(10):
#         print(num)

# num2 = 0
# while num2 < 10:
#     print(num2)
#     num2 += 1 

# num3 = 0
# while True: 
#     if num3 == 10:
#         break
#     print(num3)
#     num3 += 1 
    
# print(list(range(10)))

# string = "Hello World!"

# for i in range(len(string)):
#     print(string[i])

# for c in enumerate(string):
#     print(c)

# for num in range(5):
#     print(num)
#     if num > 3:
#         break
# else: 
#     print("why@")

# for name in range(5):
#     continue 
# print(end)
# number  = "1234"
# list = []

# list = [num for num in number]
# print(list)


# list2 = [num * 2 for num in range(2,5)]
# print(list2)

# lit3 = [num for num in range(10) if num % 2 == 0]
# print(lit3)