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

# Sort the times in descending order and get the top 10
longest_times = sorted(time_per_request, reverse=True)[:10]

# Print the results
for time in longest_times:
    print(f'Time per request: {time}')