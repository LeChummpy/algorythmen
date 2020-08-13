def loeffelsprache(text):
    TEXT = text.upper()
    result = []
    RESULT = ""

    for i in TEXT:
        
        if (i == "A" or i == "I" or i == "E" or i == "O" or i == "U"):
            result.append("AW" + i)
            
        else:
            result.append(i)

    return RESULT.join(result)


def tagebisferien(current_day, current_month):
    result = 0

    def NumberOfDaysInCurrentMonth(month):
        if (month==8):
            return 31
        elif (month==9):
            return 30
        elif (month==10):
            return 31
            
    ferienbeginn_tag = 12
    ferienbeginn_monat = 10

    if (current_day==ferienbeginn_tag and current_month==ferienbeginn_monat):
        return 0
    
    elif ( (current_day>ferienbeginn_tag and current_month==ferienbeginn_monat) or (current_month>ferienbeginn_monat)):
        return None

    else:

        iterate_day = current_day
        iterate_month = current_month
        while(True):
            result+=1

            iterate_day+=1

            if (iterate_day>=NumberOfDaysInCurrentMonth(iterate_month)):
                iterate_month+=1
                iterate_day = 1

            if (iterate_day==ferienbeginn_tag and iterate_month==ferienbeginn_monat):
                return result
            
        
        
        


        
        
