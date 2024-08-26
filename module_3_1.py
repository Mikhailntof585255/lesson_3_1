calls = 0


def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info(string):
    count_calls()
    info = string
    count = len(string)
    count1 = (string.upper())
    count2 = string.lower()
    return count, count1, count2


def is_contane(string, list):
    count_calls()
    wr = string.upper()
    for i in range(len(list)):
        b1 = False
        if wr == list[i].upper():
            b1 = True
            break
    return b1


print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contane("Urban", ['ban', 'BaNaN', 'urBAN']))
print(is_contane('cycle', ['recycling', 'cycling']))
print(calls, " вызовов функций")
