student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else: 
        student_grades[student] = "Fail"
    


print(student_grades)



capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}


#Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgard"], "total_visits":5},
}

#Nesting Dictionary in a List

travel_log = [
    {
        "country":"France",
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin", "Hamburg", "Stuttgard"],
        "total_visits":5,
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
    
add_new_country("Russia", 2,["Moscow", "Saint Petersburg"])


for items in range(len(travel_log)-1):

    print(f"{travel_log[items]}")