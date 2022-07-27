import re


def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+(@igs-software.com.br)'
    if re.search(regex,email):
        return True
    return False
        