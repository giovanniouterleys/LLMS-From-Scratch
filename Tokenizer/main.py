with open("input.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

print("Total number of characters in the text:", len(raw_text))
print(raw_text[:99])    