import random

#Creating components of story line
characters = ["a king" , "a queen" , "a dragon", "a wizard"]
places = ["in a castle","in a forest","on the mountain","in a graveyard"]
actions = ["found","fought","rescued","discovered"]
objects = ["a treasure","a spell book","a magic sword","a unicorn"]

def generate_story():
    character=random.choice(characters)
    place=random.choice(places)
    action=random.choice(actions)
    object=random.choice(objects)

    story = f"One day, {character} {place} {action} {object}."
    return story

def main():
    print("Welcome user to the Random story generator!")
    while True:
        print("\n Your random story:")
        print(generate_story())

        again = input("\n Do you want to generate another story?(yes/no)").strip().lower()
        if again != 'yes':
            break
    print("Thank you! see you again")

if __name__ =="__main__":
    main()