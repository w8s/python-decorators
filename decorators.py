data = [
    {"name": "Buffy", "role": "Slayer", "weapon": "Stake"},
    {"name": "Willow", "role": "Witch", "weapon": "Magic"},
    {"name": "Xander", "role": "Whiner", "weapon": "Zepplin"},
    {"name": "Anya", "role": "Ex-Demon", "weapon": "Capitalism"},
]

strength = {"Slayer": 10, "Witch": 4, "Whiner": 2, "Ex-Demon": 8}

wisdom = {"Slayer": 6, "Witch": 9, "Whiner": 2, "Ex-Demon": 4}


def list_characters():
    for c in data:
        print(c["name"])
    print()


def list_roles():
    for c in data:
        print("%s: %s" % (c["name"], c["role"]))
    print()


def list_weapons():
    for c in data:
        print("%s: %s" % (c["name"], c["weapon"]))
    print()

def list_stronger():
    for c in data:
        if strength[c["role"]] > 6:
            print("%s: %s" % (c["name"], strength[c["role"]]))
    print()

def list_wiser():
    for c in data:
        if wisdom[c["role"]] > 6:
            print("%s: %s" % (c["name"], wisdom[c["role"]]))
    print()


def main():
    print("Characters")
    print("==========")
    list_characters()

    print("Roles")
    print("=====")
    list_roles()

    print("Weapons")
    print("=======")
    list_weapons()

    print("Stronger than 6")
    print("===============")
    list_stronger()

    print("Wiser than 6")
    print("===============")
    list_stronger()


if __name__ == "__main__":
    main()
