import re


def alphanumeric(password):
    if len(password) > 0 and re.match("^[A-Za-z0-9]*$", password):
        return True
    else:
        return False


alphanumeric("hello world_")
alphanumeric("PassW0rd")
alphanumeric("     ")
