def collapse(value):   
    total = 0
    remainingDigits = len(value)
    
    if isinstance(value,str) and value.isnumeric() and remainingDigits < 51:
    
        while remainingDigits == 1:
            return value
    
        while remainingDigits > 1:
            total = 0
            for i in value:
                total += int(i)
                value = str(total)
                remainingDigits = len(str(total))
    
        return value
    else:
        return None