import re


def name_validation(input_name):
    if not 5 < len(input_name) < 14:
        return False
    res = re.findall('[a-zA-Z]*', input_name)
    if len(res) == 1:
        return True
    else:
        return False




def email_validation(input_email):
    res = re.findall('(\w)+(\@{1})(\w)+(\.{1})(\w)+', input_email)
    if len(res) == 1:
        return True
    else:
        return False


def phone_validation(input_number):
    res = re.findall('[09](\d{9})+|[+98](\d{11})+', input_number)
    if len(res) == 1:
        return True
    else:
        return False


print(name_validation('Amir52'))
print(phone_validation('09011111111'))
print(email_validation('amir@gmail.com'))
