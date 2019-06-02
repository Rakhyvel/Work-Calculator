### Work Calculator
### Author: Joseph Shimel
### Description: A program that tells the user how far a long their shift they are.

CENTS_PER_HOUR = 1150.0/1.08
BREAK_LENGTH = 60

def main():
  '''
  This function is responsible for gathering information, then starting the time loop
  '''
  start_time, end_time, break_time = setup()
  shift_length = (end_time-start_time)
  if break_time != -1:
    shift_length -= BREAK_LENGTH
  total_money = calc_money(shift_length)
  print("Shift length:", convert_to_string(shift_length))
  print("Money made during shift: $"+str(total_money))
  # Start time loop
  time_loop(start_time, end_time, break_time, shift_length)

def setup():
  '''
  This function is responsible for getting start, end, and break times from user
  start_time = int(get_minutes_since_midnight(input("Start of shift: ")))
  end_time = int(get_minutes_since_midnight(input("End of shift: ")))
  break_time = int(get_minutes_since_midnight(input("Break?: ")))
  '''
  start_time = int(get_minutes_since_midnight("8:00"))
  end_time = int(get_minutes_since_midnight("6:00"))
  break_time = int(get_minutes_since_midnight("12:00"))
  if end_time < start_time:
    end_time += 12*60
  if break_time < start_time and break_time != -1:
    break_time += 12*60
  return start_time, end_time, break_time

def calc_money(minutes_into_shift):
  '''
  This function is responsible for calculating the money made based on minutes worked
  '''
  return int((minutes_into_shift/60.0)*CENTS_PER_HOUR)/100.0

def time_loop(start_time, end_time, break_time, shift_length):
  while True:
    # Get time and convert it
    current = get_minutes_since_midnight(input("\nTime: "))
    # If MSM of current is less than MSM of start, add 12 hours
    if current < start_time:
      current += 12*60
    if current > break_time and break_time != -1:
      if current < break_time+60:
        current = break_time
      else:
        current -= BREAK_LENGTH
    # Get percent
    percent = (current-start_time)/shift_length
    # Print results to terminal
    if percent >= .983:
      time_left = "shift complete!"
    else:
      time_left = convert_to_string((1-percent)*shift_length)+"left"
    print(str(int(100*percent))+"% complete, $" + str(calc_money(current-start_time)), "made so far,",time_left)
    print_bar(start_time, end_time, break_time, current)

def convert_to_string(minutes):
  '''
  Given the amount of minutes since midnight, returns
  '''
  hours = int(minutes/60)
  minutes -= (hours * 60)
  hour_string = get_quantity_string(hours,"hour")
  minute_string = get_quantity_string(minutes,"minute")
  return hour_string + minute_string

def get_minutes_since_midnight(time):
  '''
  Given a string presuming two integers seperated by a colon, returns the number of minutes the time would be since midnight
  '''
  if time == "":
    return -1
  time = time.split(":")
  hours = int(time[0])
  minutes = int(time[1])
  return hours*60+minutes

def get_quantity_string(quantity, name):
  '''
  Returns a properly formatted string that reads off how many of a quantity there is.
  Ex: quanity = 3, name = hour
  Returns: "3 hours"
  '''
  quantity_string = str(int(quantity)) + " " + name
  if quantity > 1:
    # Hours are plural
    quantity_string += "s "
  elif quantity == 1:
    # Hours are one
    quantity_string += " "
  else:
    # No hours
    quantity_string = ""
  return quantity_string

def print_bar(start_time, end_time, break_time, current_time):
  '''
  This function draws a progress bar given details about the shift
  '''
  print("│", end = "")
  if break_time != -1 and current_time > break_time:
    current_time += BREAK_LENGTH
  i = start_time
  hour = 60
  while i < end_time:
    if i >= break_time and i < break_time + BREAK_LENGTH and break_time != -1:
      print(" ", end = "")
    elif i < current_time:
      print("█", end = "")
    else:
      print("░", end = "")
    i+=(end_time-start_time)/60.0
  print("│")

main()
