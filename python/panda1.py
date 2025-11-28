import panda as pd

def greet():
    return pd.get_greeting() + ", Panda!"

if __name__ == "__main__":
    print(greet())
    