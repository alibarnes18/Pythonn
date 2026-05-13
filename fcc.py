def create_character(name, strength, intelligence, charisma):

    # Name validations
    if not isinstance(name, str):
        return "The character name should be a string."

    if name == "":
        return "The character should have a name."

    if len(name) > 10:
        return "The character name is too long."

    if " " in name:
        return "The character name should not contain spaces."


    stats = [strength, intelligence, charisma]

    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers."

    if not all(stat >= 1 for stat in stats):
        return "All stats should be no less than 1."

    if not all(stat <= 4 for stat in stats):
        return "All stats should be no more than 4."

    if sum(stats) != 7:
        return "The character should start with 7 points."

    # Function to create stat line
    def build_stat(label, value):
        return f"{label} {'●' * value}{'○' * (10 - value)}"

    # Final character sheet
    return (
        f"{name}\n"
        f"{build_stat('STR', strength)}\n"
        f"{build_stat('INT', intelligence)}\n"
        f"{build_stat('CHA', charisma)}"
    )