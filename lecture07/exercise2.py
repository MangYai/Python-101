performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90],
        "Bob": [70, 75, 78, 80],
        "Charlie": [60, 65, 70, 72]
    },
    "Engineering": {
        "David": [90, 92, 94, 95],
        "Eve": [85, 88, 87, 90],
        "Frank": [88, 87, 86, 85]
    },
    "HR": {
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73],
        "Ivan": [60, 62, 64, 66]
    }
}

average_scores = {}
for department, employees in performance_data.items():
    average_scores[department] = {}
    for employee, scores in employees.items():
        average = sum(scores) / len(scores)
        average_scores[department][employee] = average
print(average_scores)

top_performers = {}
for department, employees in average_scores.items():
    top_employee = max(employees, key=employees.get)
    top_performers[department] = (top_employee, employees[top_employee])
print(top_performers)

best_department = max(average_scores, key=lambda d: sum(average_scores[d].values()) / len(average_scores[d]))
best_department_avg = sum(average_scores[best_department].values()) / len(average_scores[best_department])
print(best_department, best_department_avg)

continuous_improvers = {}
for department, employees in performance_data.items():
    improvers = []
    for employee, scores in employees.items():
        if all(scores[i] < scores[i + 1] for i in range(len(scores) - 1)):
            improvers.append(employee)
    continuous_improvers[department] = improvers
print(continuous_improvers)

print("Summary Report:")
for department, employees in average_scores.items():
    print("Department:", department)
    for employee, avg in employees.items():
        print(" ", employee, "Average Score =", round(avg, 2))
    top_employee, top_avg = top_performers[department]
    print("Top Performer:", top_employee, "with Average Score =", round(top_avg, 2))
print("Best Department:", best_department, "with Average Score =", round(best_department_avg, 2))