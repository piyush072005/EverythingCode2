import random

activities = [
    "Read a sci-fi short story",
    "Take a 10-minute walk",
    "Try a new coffee brew",
    "Solve one coding puzzle",
    "Sketch something you see"
]

if __name__ == "__main__":
    print("You should:", random.choice(activities))