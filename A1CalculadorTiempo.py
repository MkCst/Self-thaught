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
    period_dayDict = {"AM": "PM", "PM": "AM"}

    # CANTIDAD DE DIAS TRANSCURRIDOS
    amount_days = duration_hours // 24
    print("Dias transcurridos: ", amount_days)

    # Minutos establecidos
    minutes_assigned = start_minutes + duration_minutes
    # Asignando horas
    if(minutes_assigned >= 60):
        start_hours += 1
        minutes_assigned = minutes_assigned % 60
    iteration_ampmCount = (start_hours + duration_hours) // 12
    
    hours_assignated = (start_hours + duration_hours) % 12
    print("Horas asignadas",hours_assignated)
    print("Minutos asignados", minutes_assigned)


# Simulacion de main
print(add_time("1:00 AM", "10:59", "Monday"))
