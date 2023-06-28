class Man:
    def __init__(self,name,age,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
        self.age=age


class DietSchedule:
    def __init__(self,calories_goal,protein_goal,fat_goal):
        self.calories_goal=calories_goal
        self.protein_goal=protein_goal
        self.fat_goal=fat_goal
        self.calories=0
        self.protein=0
        self.fat=0


    def dish(self,name,calories,protein,fat):
        self.calories+=calories

        self.fat+=fat

        self.protein+=protein

        print(f"Your dish {name} gave You {protein} protein, {fat} fat and {calories} calories")


    def burning(self,name,calories_burnt):
        self.calories-=calories_burnt
        self.name=name
        print(f"Your training {name} burnt {calories_burnt} of your daily calories")




    def show_results(self,):
        remaining_calories=self.calories_goal-self.calories
        if remaining_calories<=0:
            print("Your calories goal is completed")
        remaining_fat=self.fat_goal-self.fat
        if remaining_fat<=0:
            print("Your fat goal is completed")
        remaining_protein=self.fat_goal-self.fat
        if remaining_protein<=0:
            print("Your protein goal is completed")

        print(f"Results for {self.name} :")
        print(f"Protein goal: {remaining_protein}")
        print(f"Fat's goal: {remaining_fat}")
        print(f"Calories's goal: {remaining_calories}")

        if remaining_calories>=0 and remaining_fat>=0 and remaining_protein>=0:
            print("Congratulations, Your gain is achieved")
        else:
            print("Unfortunately You still have to work on Your daily diet")

john=Man("John",30,80,180)

diet=DietSchedule(2000,180,80)

diet.dish("Breakfast",500,20,10)
diet.dish("Lunch", 800, 40, 20)
diet.dish("Dinner", 700, 30, 15)

diet.burning("Running",300)

diet.show_results()

