f_name = input("What is your first name?\n")
l_name = input("What is your last name?\n")


def format_name(name, last_name):
    formated_name = name.title()
    formated_last_name = last_name.title()
    return f"{formated_name} {formated_last_name}"


print(format_name(f_name, l_name))
