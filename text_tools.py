# Задание 2
def clean_notice(text):
    words=text.split()
    return " ".join(words)
print(clean_notice(" EKEB ждёт T118! "))
print(clean_notice("Алматы\nАстана\tТараз"))
print(clean_notice(" "))

# Задание 3
def has_bug(text):
    return "bug" in text.lower()
print(has_bug("BUG найден"))
print(has_bug("Найден bug"))
print(has_bug("DEBUG"))
print(has_bug("Всё работает"))
print(has_bug(""))

# Задание 4
def valid_nickname(text):
    if len(text)<4 or len(text)>12:
        return False
    first_char=text[0]
    if first_char not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
        return False
    allowed_chars="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789_"
    for char in text[1:]:
        if char not in allowed_chars:
            return False
    return True
print(valid_nickname("Aruzhan_7"))
print(valid_nickname("A12"))
print(valid_nickname("7Aruzhan"))

# Задание 5
def preview(text,limit):
    cleaned=" ".join(text.split())
    if len(cleaned)<=limit:
        return cleaned
    else:
        return cleaned[:limit-3]+"..."
print(preview("EKEB приглашает", 10))
print(preview(" EKEB",4))