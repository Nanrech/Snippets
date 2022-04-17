import json
import random

with open("albums.json", "r") as f:
    dictionario = json.load(f)
keys = list(dictionario.keys())
artists = [dictionario[album]['artist'] for album in keys]
randomized = keys[random.randint(0, len(dictionario))]
print(f"Today's album is '{randomized}', by '{dictionario[randomized]['artist']}'")
while True:
    print("-" * 22)
    search = input("\t> Input album name: ")
    if search == "!stop":
        exit()
    results: list = [string for string in keys if search.lower() in string.lower()]
    if len(results) == 0:
        separator = "-" * 22
    else:
        separator = "-" * (len(max(results, key=len)) + 8 + len(dictionario[max(results, key=len)]["artist"]))
    print(separator)
    print("\n".join([f"'{result}' by '{dictionario[result]['artist']}'" for result in results]) or "\t> No results found")
    if len(results) != 0:
        print(f"\t> Found {len(results)} results")
