def format_name(f_name, l_name):
    """
    Takes two parameters: first name and last name.
    Turns each string into title case and returns both as an f-string
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



