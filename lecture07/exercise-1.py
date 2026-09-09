survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"]
]

survey_sets = [set(choices) for choices in survey_results]

chosen_by_all = set.intersection(*survey_sets)
print(chosen_by_all)

all_languages = set.union(*survey_sets)
counts = {lang: sum(lang in s for s in survey_sets) for lang in all_languages}

chosen_by_one = {l for l, c in counts.items() if c == 1}
print(chosen_by_one)

unique_languages_count = len(all_languages)
print(unique_languages_count)

chosen_by_two = {l for l, c in counts.items() if c == 2}
print(chosen_by_two)

same_choices = []
for i in range(len(survey_sets)):
    for j in range(i + 1, len(survey_sets)):
        if survey_sets[i] == survey_sets[j]:
            same_choices.append([i + 1, j + 1])
print(same_choices)