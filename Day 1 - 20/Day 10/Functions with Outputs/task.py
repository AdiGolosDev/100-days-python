def format_name(f_name, l_name):
    """takes first name and last name and changes it into title case"""
    format_f = f_name.title()
    format_l = l_name.title()

    return f"{format_f} {format_l}"

print(format_name("klEIn", "moReTti"))