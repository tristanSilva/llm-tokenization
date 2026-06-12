# This is a baby tokenizer - it splits the sentence into word-level tokens
def baby_token(sentence="The quick brown fox jump over the lazy dog"):

    tokens = sentence.split(" ")

    for index, token in enumerate(tokens):
        print(f"Token {index}: '{token}'")

    print(f"\nTotal tokens: {len(tokens)}")


if __name__ == "__main__":
    response = input("What would you like to say? ")
    baby_token(response)
