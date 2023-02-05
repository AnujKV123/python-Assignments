
# 5. participants_list = [
#     ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
#     ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
#     ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
#     ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
#     ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
#     ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
#     ]
# print("daily_participants---------")
# daily_participants(participants_list) # ['Desmond', 'Krish', 'Sam']
# print("one_time_participants---------")
# one_time_participants(participants_list)# ['Kapil', 'Ron', 'Ginny', 'Ted', 'Sachin', 'John', 'Joan']
# print("first_day_only_participants----------------")
# first_day_only_participants(participants_list) #  ['John', 'Joan']

def daily_participants(pCount, lst):
    dailyParticipants = []
    for p, q in pCount.items():
        if q == len(lst):
            dailyParticipants.append(p)
    return dailyParticipants


def one_time_participants(pCount, lst):
    oneTimeParticipants = []
    for p, q in pCount.items():
        if q == 1:
            oneTimeParticipants.append(p)
    return oneTimeParticipants

def first_day_only_participants(pCount, lst):
    firstDayOnlyParticipants = []
    for item in lst[0]:
        if item in pCount and pCount[item] == 1:
            firstDayOnlyParticipants.append(item)
    return firstDayOnlyParticipants

participants_list = [
    ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
    ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
    ]

pCount = {}
for item in participants_list:
    for i in item:
        if i not in pCount:
            pCount[i]=1
        else:
            pCount[i] += 1

print("daily_participants---------")
print("List of Daily participants: ", daily_participants(pCount, participants_list))
print("\n")
print("one_time_participants---------")
print("List of one time participants: ", one_time_participants(pCount, participants_list))
print("\n")
print("first_day_only_participants----------------")
print("List of first day only participants: ", first_day_only_participants(pCount, participants_list))