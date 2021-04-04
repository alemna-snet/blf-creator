import textwrap

def is_blank(x: list) -> bool:
    for item in x:
        if item != "":
            return False
        else:
            pass
    return True


def print_block(text: str, width=77):
    print(textwrap.fill(text, width))


def print_item(text):
    print()
    if isinstance(text, str):
        print(f"    {text}")
    elif isinstance(text, (list, tuple, set)):
        for item in text:
            print(f"    {item}")
    else:
        raise TypeError(text)
    print()