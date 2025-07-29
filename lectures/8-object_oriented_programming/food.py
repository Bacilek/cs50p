class Food:
    base_hearts = 1  # class variable
    
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)
    
    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts
    
    # no ingredient specified, choose hearts count
    @classmethod
    def from_nothing(cls, hearts):
        food = cls(ingredients=[])
        food.hearts = hearts
        return food
        


def main():
    mushroom_skewer = Food(["Mushroom", "Hearty Mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")
    
    melon = Food.from_nothing(hearts=3)
    print(f"This melon heals {melon.hearts} hearts!")

main()