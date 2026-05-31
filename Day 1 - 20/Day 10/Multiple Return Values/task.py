def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("KLeIn", "MorETtI"))

def canBuyAlcohol(age):
    if age > 17:
        return True
    else:
        return False

def canBuyAlcohol2(age):
    if type(age) != int:
        return

    if age > 17:
        return True
    else:
        return False
