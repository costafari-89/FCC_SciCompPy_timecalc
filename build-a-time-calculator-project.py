def add_time(start, duration, day=""):
    def split_time(time_string):
            
        #Split start time by : to seperate hour and min
        start_split = time_string.split(':')
        
        #Pull hour and minute and make integer
        hour = start_split[0]
        minute = start_split[1][:2]
        
        #Make hour and minute integers
        hour_int = int(hour)
        minute_int = int(minute)

        return hour_int, minute_int

    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_of_week_lower = [i.lower() for i in days_of_week]
    weekday_index = 0
    weekday = ""
    start_hour, start_min = split_time(start)
    dur_hour, dur_min = split_time(duration)
    start_ampm = start[-2:]
    
    #Converting to 24hr clock
    if start_ampm == "PM":
        start_hour += 12
    
    new_min = start_min + dur_min

    #determing additional hr from min addition using floor division
    hour_f_min = new_min//60

    #assigning new minute as left over after adding additional hour to hours
    new_min = new_min % 60
    new_hour = start_hour + dur_hour + hour_f_min

    #Determining number of days that have passed and redefining 24hr  
    num_days = new_hour//24
    new_hour = new_hour%24

    #Determining index of weekday when optional argument given
    if day != "":
        weekday_index = days_of_week_lower.index(day.lower())
        weekday = days_of_week[weekday_index]

    #Determining additional strings for when we pass to another day and also defining weekday for that next day or days
    if num_days == 1:
        extra_string = "(next day)"
        weekday_index = (num_days + weekday_index)%7
        weekday = days_of_week[weekday_index]
    elif num_days > 1:
        extra_string = "(" + str(num_days) + " days later)"
        weekday_index = (num_days + weekday_index)%7
        weekday = days_of_week[weekday_index]
    else:
        extra_string = ""

    #Add print strings to work with hours and minutes before trying to format
    # print(days_of_week_lower)
    # print(num_days)
    # print(new_hour)
    # print(new_min)

    #Adding 0 to string for all minutes below 10
    if new_min < 10:
        new_min = '0'+str(new_min)

    #Editing string components of hour when passing 12
    if new_hour > 12:
        new_ampm = 'PM'
        new_hour = new_hour%12
    elif new_hour == 12:
        new_hour = 12
        new_ampm = 'PM'
    elif new_hour == 0:
        new_hour = 12
        new_ampm = 'AM'
    else:
        new_ampm = 'AM'

    #Creating strings to be returned based on input arguments provided
    time_string = str(new_hour) + ":" + str(new_min)
    time_return = time_string + " " + new_ampm
    time_return_day = time_string + " " + new_ampm + ' ' + extra_string
    time_return_weekday = time_string + " " + new_ampm + ', ' + weekday + ' ' + extra_string
    
    if day != "":
        return time_return_weekday.strip()
    elif num_days >= 1:
        return time_return_day
    else:
        return time_return
    
print(add_time('3:30 PM', '2:12', 'Monday')) 
