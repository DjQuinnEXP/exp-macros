import re

# Read the log file
with open('salesforce_stresstest.log', 'r') as file:
    log_data = file.readlines()

# Extract "time per request" values
time_per_request = []
for line in log_data:
    match = re.search(r'Time per request: (\d+\.\d+)', line)
    if match:
        time_per_request.append(float(match.group(1)))

# Calculate the average time per request
if time_per_request:
    average_time = sum(time_per_request) / len(time_per_request)
    print(f'Average time per request: {average_time}')
else:
    print('No "time per request" values found in the log file.')