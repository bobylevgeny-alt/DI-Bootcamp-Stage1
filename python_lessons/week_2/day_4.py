# class Animal:
#     def __init__(self, food_amount, food_type):
#         self.food_amount = food_amount
#         self.food_type = food_type


# class Wolf(Animal):
#     def __init__(self):
#         self.food_amount = 2
#         self.food_type = "meat"


# class Parrot(Animal):
#     def __init__(self):
#         self.food_amount = 0.2
#         self.food_type = "fruit"


# class Chicken(Animal):
#     def __init__(self):
#         self.food_amount = 0.15
#         self.food_type = "wheat"

# zoo = [Animal (2, 'meat'), 
#        Animal (0.2, "fruit"), 
#        Animal (0.15, "wheat")
#        ]


# zoo = [
#     Wolf(),
#     Wolf(),
#     Parrot(),
#     Parrot(),
#     Parrot(),
#     Chicken()
# ]



# days = int(input("Enter number of days: "))

# meat = 0
# fruit = 0
# wheat = 0

# for animal in zoo:
#     if animal.food_type == "meat":
#         meat += animal.food_amount * days

#     elif animal.food_type == "fruit":
#         fruit += animal.food_amount * days

#     elif animal.food_type == "wheat":
#         wheat += animal.food_amount * days


# print(f"Meat: {meat} kg")
# print(f"Fruit: {fruit} kg")
# print(f"Wheat: {wheat} kg")


