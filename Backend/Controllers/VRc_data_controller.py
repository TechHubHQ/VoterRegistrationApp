import os
import json

# Load the JSON file
json_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "ui", "scripts", "json", "us_states_cities.json")
with open(json_file, 'r') as file:
    data = json.load(file)

# Create a dictionary to store unique cities for each state
filtered_data = {}

# Iterate through states and their cities to collect unique names
for state, cities in data.get('USA', {}).items():
    unique_cities = set(cities)  # Create a set to remove duplicates
    sorted_cities = sorted(unique_cities)  # Sort cities alphabetically
    filtered_data[state] = sorted_cities

# Wrap the filtered data in a top-level dictionary with the key 'USA'
final_data = {'USA': filtered_data}

# Write the filtered and sorted data back to a JSON file
with open('us_states_cities_noduplicate_name.json', 'w') as file:
    json.dump(final_data, file, indent=2)
