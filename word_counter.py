def count_words(text):
    return len(text.split())


def main():
    print("\n===== WORD COUNTER =====")

    text = input("Enter a sentence or paragraph: ")

    if not text.strip():
        print("Please enter some text.")
        return

    words = count_words(text)
    characters = len(text)
    characters_without_spaces = len(text.replace(" ", ""))

    print("\n===== RESULT =====")
    print(f"Word Count                 : {words}")
    print(f"Character Count            : {characters}")
    print(f"Characters Without Spaces  : {characters_without_spaces}")


if __name__ == "__main__":
    main()
