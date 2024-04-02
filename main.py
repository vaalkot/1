# Коллбэки
def ask_password(login, password, success, failure):
    glas = ['a', 'e', 'i', 'o', 'u', 'y']
    soglas = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    g = 0
    s = 0
    p = ''
    p1 = ''
    for el in password:
        if el in login and el in glas:
            g += 1
        if el in login and el in soglas:
            s += 1
            p += el
        for b in login:
            if b in soglas:
                p1 += b

        if g == 3 and s == 3 and p == p1:
            success = login.lower()
        else:
            if g != 3 and p == p1:
                failure = 'Wrong number of vowels'
            if p != p1 and g == 3:
                failure = 'Wrong consonants'
            if g != 3 and p != p1:
                failure = 'Everything is wrong'
        return
            # return login.lower(), password.lower()



def main(login, password):
    pass


