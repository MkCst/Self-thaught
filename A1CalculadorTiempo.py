def add_time(start, duration, day_of_week=False):
    day_of_week_index = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }
    day_of_week_array = [
        "Monday", "Tuesday",
        "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

    # DURACION
    # Definicion
    duration_tuple = duration.partition(":")
    print("Tupla duracion:\t", duration_tuple)
    # asignacion
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])

    # TIEMPO INICIAL
    # definicion
    start_tuple = start.partition(":")
    start_2do_arg = start_tuple[2].partition(" ")
    print("Tiempo inicial:\t", start_tuple)
    # asignacion
    start_hours = int(start_tuple[0])
    start_minutes = int(start_2do_arg[0])

    # PERIODO DEL DIA
    period_day = start_2do_arg[2]
    set_period = {"AM": "PM", "PM": "AM"}

    # CANTIDAD DE DIAS TRANSCURRIDOS
    amount_days = duration_hours // 24
    
    # Minutos establecidos
    minutes_assigned = start_minutes + duration_minutes
    # Asignando horas y minutos
    if(minutes_assigned >= 60):
        start_hours += 1
        minutes_assigned = minutes_assigned % 60
    iteration_ampmCount = (start_hours + duration_hours) // 12
    hours_assignated = (start_hours + duration_hours) % 12
    print("Horas asignadas", hours_assignated)
    print("Minutos asignados", minutes_assigned)

    # APLICANDO FORMATO
    minutes_assigned = minutes_assigned if minutes_assigned > 9 else "0" + \
        str(minutes_assigned)
    hours_assignated = hours_assignated = 12 if hours_assignated == 0 else hours_assignated
    if(period_day=="PM" and start_hours +(duration_hours%12)>=12):
       amount_days+=1
    print(hours_assignated, minutes_assigned, period_day)
    print("numero de dias:", amount_days)
    
    # ESTABLECIENDO HORARIO
    period_day = set_period[period_day] if iteration_ampmCount % 2 == 1 else period_day
    # ESTABLECIENDO DIA
    if (day_of_week):
        day_of_week = day_of_week.lower()
        index = int((day_of_week_index[day_of_week]) + amount_days) % 7
        newday = day_of_week_array[index]


    # FORMATO DE REGRESO
    result_time = str(hours_assignated) + ":" + str(minutes_assigned) + " "+period_day
    days_later = "(next day)" if amount_days == 1 else "(" + str(amount_days)+" days later)"
    
    if (amount_days >= 1 and day_of_week==False):
        result_time +=" "+days_later
    if (amount_days>=1 and day_of_week):
        result_time+= ", "+newday+" "+days_later
    if (amount_days==0 and day_of_week):
        result_time+= ", "+newday
    return result_time 


# Simulacion de main
print(add_time("6:30 PM","205:12"))
