import itertools
from math import radians, sin, cos, sqrt, atan2

# Mean radius of the Earth in kilometers
EARTH_RADIUS = 6371.0

# City bank branch locations with longitude and latitude coordinates
branches = [
    ("City Bank Uttara Branch", 23.8728568, 90.3984184),
    ("City Bank Dhanmondi Branch", 23.7460614, 90.3768222),
    ("City Bank Gulshan Branch", 23.7919689, 90.4179393),
    ("City Bank Mirpur Branch", 23.8043457, 90.3698377),
    ("City Bank Banani Branch", 23.7940297, 90.4133763),
    ("City Bank Mohammadpur Branch", 23.7651524, 90.3636335),
    ("City Bank Motijheel Branch", 23.7292864, 90.4103905),
    ("City Bank Wari Branch", 23.7070712, 90.4177887),
    ("City Bank Jatrabari Branch", 23.7007489, 90.4285994),
    ("City Bank Savar Branch", 23.8483408, 90.2476963)
]

# Function to calculate the distance between two branches (based on longitude and latitude)
def calculate_distance(branch1, branch2):
    lon1, lat1 = branch1[1], branch1[2]
    lon2, lat2 = branch2[1], branch2[2]

    # Convert coordinates from degrees to radians
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lon2 = radians(lon2)
    lat2 = radians(lat2)

    # Difference in longitude and latitude
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate the distance
    distance = EARTH_RADIUS * c

    return distance

# Generate all possible permutations of branch visits
permutations = list(itertools.permutations(branches))

# Initialize variables to store the best route and minimum distance
best_route = None
min_distance = float("inf")  # Initialize with a large value

# Iterate over all permutations and find the route with the minimum distance
for route in permutations:
    distance = 0
    for i in range(len(route) - 1):
        branch1 = route[i]
        branch2 = route[i + 1]
        distance += calculate_distance(branch1, branch2)
    if distance < min_distance:
        min_distance = distance
        best_route = route

# Print the best route and minimum distance
print("Best Route:")
for branch in best_route:
    print(branch[0])
print("Minimum Distance:", min_distance, "kilometers")
