
def parse_accuracy_string(accuracy: str) -> str:
    """
    Parses the accuracy string, returning a deterministic, formatted string.

    Example:
        ```
        parse_accuracy_string("MIG+MIG+2+4")   # returns "【MIG+MIG】+6"
        ```
    """

    ACCEPTED_KEYWORDS = ["DEX", "INS", "MIG", "WLP"]

    i = 0
    attribs = []
    bonus = 0
    while i < len(accuracy):
        match accuracy[i]:
            case '(' | '[' | '【' | '{':
                i += 1
            case ')' | ']' | '】' | '}':
                i += 1
            case ' ' | '\t':
                i += 1
            case '+':  #TODO: I'm assuming there's no negatives here
                i += 1
            case _:
                if accuracy[i].isdigit():
                    # Parse until not a digit anymore
                    j = i + 1
                    while j < len(accuracy) and accuracy[j].isdigit():
                        j += 1

                    # Invariant: j is now end of string OR pointing to a non-digit
                    number = int(accuracy[i:j])
                    bonus += number
                    i = j
                elif accuracy[i].isalpha():
                    # Parse until we get a full keyword (only alphabetical chars)
                    j = i + 1
                    while j < len(accuracy) and accuracy[j].isalpha():
                        j += 1

                    # Invariant: j is now end of string OR pointing to a non-character
                    keyword = accuracy[i:j]
                    found = False
                    for test_keyword in ACCEPTED_KEYWORDS:
                        if test_keyword == keyword:
                            found = True

                    if not found:
                        raise ValueError(f"parse_accuracy_string: Invalid keyword {keyword}")
                    attribs.append(keyword)
                    i = j
                else:
                    raise ValueError(f"parse_accuracy_string: Unexpected character {accuracy[i]}")

    # Construct result string
    res_accuracy = ""
    attribs = sorted(attribs)  # Ensure sorted order of attributes -- they're in alphabetical order, what a fortunate coincidence!
    if len(attribs) != 0:
        res_accuracy += "【" + "+".join(attribs) + "】"
    if bonus != 0:
        res_accuracy += f"+{bonus}"

    return res_accuracy


def parse_damage_string(damage: str) -> str:
    """
    Parses the damage string, returning a deterministic, formatted string.

    Example:
        ```
        parse_damage_string("2+4+HR+4+HR")   # returns "【HR+HR】+10"
        ```
    """

    ACCEPTED_KEYWORDS = ["HR", "LR"]  # Not too sure if LR exists, but just in case :)

    i = 0
    keywords = []
    bonus = 0
    while i < len(damage):
        match damage[i]:
            case '(' | '[' | '【' | '{':
                i += 1
            case ')' | ']' | '】' | '}':
                i += 1
            case ' ' | '\t':
                i += 1
            case '+':  #TODO: I'm assuming there's no negatives here
                i += 1
            case _:
                if damage[i].isdigit():
                    # Parse until not a digit anymore
                    j = i + 1
                    while j < len(damage) and damage[j].isdigit():
                        j += 1

                    # Invariant: j is now end of string OR pointing to a non-digit
                    number = int(damage[i:j])
                    bonus += number
                    i = j
                elif damage[i].isalpha():
                    # Parse until we get a full keyword (only alphabetical chars)
                    j = i + 1
                    while j < len(damage) and damage[j].isalpha():
                        j += 1

                    # Invariant: j is now end of string OR pointing to a non-character
                    keyword = damage[i:j]
                    found = False
                    for test_keyword in ACCEPTED_KEYWORDS:
                        if test_keyword == keyword:
                            found = True

                    if not found:
                        raise ValueError(f"parse_damage_string: Invalid keyword {keyword}")
                    keywords.append(keyword)
                    i = j
                else:
                    raise ValueError(f"parse_damage_string: Unexpected character {damage[i]}")

    # Construct result string
    res_damage = ""
    keywords = sorted(keywords)  # We just ensure HR comes before LR
    if len(keywords) != 0:
        res_damage += "【" + "+".join(keywords) + "】"
    if bonus != 0:
        res_damage += f"+{bonus}"

    return res_damage


def parse_defense_string(defense: str) -> str:
    """
    Parses the defense string, returning the defense value.
    Note that DEX, INS, MIG, WLP in this case refer to the SIZE of the dice.

    Example:
        ```
        parse_defense_string("3+DEX + 1")   # returns "DEX+4"
        ```
    """

    ACCEPTED_KEYWORDS = ["DEX", "INS", "MIG", "WLP"]

    i = 0
    keywords = []
    bonus = 0
    while i < len(defense):
        match defense[i]:
            case ' ' | '\t':
                i += 1
            case '+':  #TODO: I'm assuming there's no negatives here
                i += 1
            case _:
                if defense[i].isdigit():
                    # Parse until not a digit anymore
                    j = i + 1
                    while j < len(defense) and defense[j].isdigit():
                        j += 1

                    # Invariant: j is now end of string OR pointing to a non-digit
                    number = int(defense[i:j])
                    bonus += number
                    i = j
                elif defense[i].isalpha():
                    # Parse until we get a full keyword (only alphabetical chars)
                    j = i + 1
                    while j < len(defense) and defense[j].isalpha():
                        j += 1

                    # Invariant: j is now end of string OR pointing to a non-character
                    keyword = defense[i:j]
                    found = False
                    for test_keyword in ACCEPTED_KEYWORDS:
                        if test_keyword == keyword:
                            found = True

                    if not found:
                        raise ValueError(f"parse_defense_string: Invalid keyword {keyword}")
                    keywords.append(keyword)
                    i = j
                else:
                    raise ValueError(f"parse_defense_string: Unexpected character {defense[i]}")

    # Construct result string
    res_defense = ""
    keywords = sorted(keywords)
    if len(keywords) != 0:
        res_defense += "+".join(keywords)
    if bonus != 0:
        res_defense += f"+{bonus}"

    return res_defense

