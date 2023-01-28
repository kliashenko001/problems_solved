def is_palindrome(text):
    l = []
    k = txt.lower()
    for i in range(len(k)):
        if k[i] not in (' , . ! ? -'):
            l.append(k[i])
    # print(l)
    s = []
    for j in range(len(l) - 1, -1, -1):
        # print(l[j])
        s.append(l[j])
    # print(s)
    if l == s:
        return True
    else:
        return False


# считываем данные
#txt = input()
txt = "Standart - smallest, sell Amstrad nats."
# вызываем функцию
print(is_palindrome(txt))