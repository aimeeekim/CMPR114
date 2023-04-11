def fat_calories():
    grams_of_fat=int(input("How many grams of fat do you consume per day: "))
    calories_from_fat=grams_of_fat*9
    print("Calories fat are: ", calories_from_fat)

def carbohydrates_calories():
    grams_of_carbohydrates=int(input("How many grams of carbohydrates do you consume per day: "))
    calories_from_carbohydrates=grams_of_carbohydrates*4
    print("Calories from carbohydrates are :",calories_from_carbohydrates)

    fat_calories()
    carbohydrates_calories()