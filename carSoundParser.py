with open("carGoesVrooooom.txt") as file:
    entire_file = file.read()
    lines = entire_file.split("\n")

    dicktionary = {}

    for line in lines:
        if line.startswith("["):
            break

        if line.find("#") != -1:
            line = line.split("#")[0]

        if line == "":
            continue

        line = line.lower()

        if line.startswith("<"): # string constants
            pair = line.lstrip("<").split(">")
            dicktionary[pair[0]] = pair[1]
            continue

        if line.startswith("{"): # float constants
            pair = line.lstrip("{").split("}")
            dicktionary[pair[0]] = float(pair[1])
            continue

print(dicktionary)



