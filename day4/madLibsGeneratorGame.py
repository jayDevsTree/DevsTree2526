def funny_madlibs():
    name = input("Enter your name: ")
    animal = input("Enter an animal: ")
    food = input("Enter a food item: ")
    place = input("Enter a place: ")
    verb = input("Enter a verb ending in -ing: ")
    adjective = input("Enter an adjective: ")
    silly_word = input("Enter a silly word: ")
    object = input("Enter an object: ")

    print("\nFunny Story")
    print(f"One day, {name} was walking their {animal} while eating a {food}.")
    print(f"Suddenly, they slipped on a {object} and landed in {place}!")
    print(f"Everyone around was {verb} and yelling '{silly_word}!'")
    print(f"It was the most {adjective} day of {name}'s life!")

funny_madlibs()
