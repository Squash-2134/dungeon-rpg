def ask_text(prompt):
    while True:
        answer = input(f"{prompt} ").strip()
        if answer:
            return answer
        print("Please enter something.")


def ask_choice(prompt, options):
    """Show a numbered list and return the INDEX of the chosen option."""
    print(prompt)
    for number, label in enumerate(options, start=1):
        print(f"  {number}. {label}")
    while True:
        answer = input("> ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer) - 1
        print(f"Enter a number between 1 and {len(options)}.")


def ask_int(prompt, minimum, maximum):
    while True:
        answer = input(f"{prompt} ({minimum}-{maximum}) ").strip()
        if answer.isdigit() and minimum <= int(answer) <= maximum:
            return int(answer)
        print(f"Enter a number between {minimum} and {maximum}.")


def ask_yes_no(prompt):
    while True:
        answer = input(f"{prompt} (y/n) ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")