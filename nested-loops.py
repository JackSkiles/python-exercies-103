
#starts clock at 1 o'clock
hours = 1
#creates loop that will increment by 1 as long as hours is less than or equal to 12
while hours <= 12:


    minutes = 0
    #creates second loop that does the same for minutes within hours
    while minutes < 60:
        
        seconds = 0
        #creates third loop that does the same for seconds within minutes
        while seconds < 60:
            #prints formated results every second.
            print(f'{hours}:{minutes}:{seconds}')

           #increments seconds
            seconds = seconds + 1
        #increments minutes
        minutes = minutes + 1
    #increments hours
    hours = hours + 1