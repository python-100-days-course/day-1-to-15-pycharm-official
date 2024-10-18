# Lists and other dictionaries can be stored as a value in a dictionary

# Lists nested inside the dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Challenge: print Lille
print(travel_log["France"][1])

# 2D list, challenge: print D
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Challenge: print Stuttgart
travel_log_nested = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
print(travel_log_nested["Germany"]["cities_visited"][2])

