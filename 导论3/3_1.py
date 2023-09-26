def ten_change_two_int(count):
    result = 0
    letter = 0
    while count>1:
        letter+=1
        b = count%2
        count = count//2
        if letter==1:
            result = b
        result = result*10+count%2
    print(result)
    return
ten_change_two_int(9)
def ten_change_two_float(count):
