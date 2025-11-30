def add_time(start, duration, start_day=None):
    # Parse the start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Convert start time to 24-hour format
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0

    # Parse the duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate the new time
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
    new_hour = total_minutes // 60
    new_minute = total_minutes % 60

    # Calculate days passed
    days_passed = new_hour // 24
    new_hour = new_hour % 24

    # Convert back to 12-hour format
    if new_hour == 0:
        new_hour = 12
        new_period = 'AM'
    elif new_hour < 12:
        new_period = 'AM'
    elif new_hour == 12:
        new_period = 'PM'
    else:
        new_hour -= 12
        new_period = 'PM'

    # Format the new time
    new_time = f"{new_hour}:{new_minute:02d} {new_period}"

    # Handle day of the week
    if start_day:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days.index(start_day.capitalize())
        end_day_index = (start_day_index + days_passed) % 7
        new_time += f", {days[end_day_index]}"

    # Add day information
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time
