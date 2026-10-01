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

# Задание 6
def parse_event(line):
    parts=line.split(";")
    if len(parts)!=3:
        return None
    group=parts[0].strip().upper()
    status=parts[1].strip().upper()
    message=parts[2].strip()
    if group not in("Т118", "Т119"): #Буква Т кириллица
        return None
    if status not in("PASS", "FAIL"):
        return None
    if not message:
        return None
    return[group,status,message]
print(parse_event(" т118 ; fail ; Ошибка входа "))
print(parse_event("Т119;PASS;Проверка завершена"))
print(parse_event("T118;PASS;ok"))
print(parse_event("Т118;WAIT;OK"))

# Задание 7
def failures(lines,group):
    target_group=group.strip().upper()
    if target_group not in ("Т118" "Т119"):
        return []
    result=[]
    for line in lines:
        parsed=parse_event(line)
        if parsed is None:
            continue
        current_group,status,message=parsed
        if current_group==target_group and status=="FAIL":
            result.append(message)
    return result
events= [
    "Т118;PASS;Вход работает",
    " t118 ; fail ; Ошибка входа",
    "Т119;FAIL;Не открывается профиль",
    "Т118;FAIL;Ошибка входа",
    "Т118;FAIL",
    "не запись"
]
print(failures(events," t118 "))
print(failures(events, "Т119"))