import random

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
    ]
    return random.choice(jokes)

if __name__ == "__main__":
    print(tell_joke())
