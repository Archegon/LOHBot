import math

remaining_time = 3600
hours = math.floor(remaining_time/3600)
remaining_time = remaining_time-(3600*hours)
minutes = math.floor(remaining_time/60)
remaining_time = remaining_time-(60*minutes)
seconds = math.floor(remaining_time)

print(f'H: {hours} M: {minutes} S: {seconds}')
