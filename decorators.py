data = [
    {"name": "Buffy", "role": "Slayer", "weapon": "Stake"},
    {"name": "Willow", "role": "Witch", "weapon": "Magic"},
    {"name": "Xander", "role": "Whiner", "weapon": "Zepplin"},
    {"name": "Anya", "role": "Ex-Demon", "weapon": "Capitalism"},
]

strength = {"Slayer": 10, "Witch": 4, "Whiner": 2, "Ex-Demon": 8}

wisdom = {"Slayer": 6, "Witch": 9, "Whiner": 2, "Ex-Demon": 4}


def heading(msg):
    def dec(func):
        def new_func(*args, **kwargs):
            print(msg)
            print("=====")
            func(*args, **kwargs)
            print()

        return new_func

    return dec


@heading("Characters")
def list_characters():
    for c in data:
        print(c["name"])


@heading("Roles")
def list_roles():
    for c in data:
        print("%s: %s" % (c["name"], c["role"]))


@heading("Weapons")
def list_weapons():
    for c in data:
        print("%s: %s" % (c["name"], c["weapon"]))


@heading("Stronger than x")
def list_stronger():
    for c in data:
        if strength[c["role"]] > 6:
            print("%s: %s" % (c["name"], strength[c["role"]]))


@heading("Wiser than x")
def list_wiser():
    for c in data:
        if wisdom[c["role"]] > 6:
            print("%s: %s" % (c["name"], wisdom[c["role"]]))


def main():
    list_characters()
    list_roles()
    list_weapons()
    list_stronger()
    list_stronger()


if __name__ == "__main__":
    main()
