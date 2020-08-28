colors = ['red', 'yellow', 'blue', 'green', 'orange']

for item in colors :
    print(item)

wish_travel_city = {
    "bangkok": "Taii",
    "LA": "USA",
    "manila": "Philippines"
}

for key in wish_travel_city:
    print(wish_travel_city[key])

for value in wish_travel_city.values():
    print(value)

for key, value in wish_travel_city.items():
    print(key + ' : ' + value)


addresses = {
    '1': {'name': 'hong kildong1', 'email': 'hong1@mail.com'},
    '2': {'name': 'hong kildong2', 'email': 'hong2@mail.com'},
    '3': {'name': 'hong kildong3', 'email': 'hong3@mail.com'},
    '4': {'name': 'hong kildong4', 'email': 'hong4@mail.com'},
}

for key in addresses:
    my_dict = addresses[key]
    print(my_dict)

# random module
import random

for i in range(10):
    print(random.randint(1, 6))

message = "I love you .. I like a honey"

counter = {}
for char in message:
    counter[char] = counter.setdefault(char, 0) + 1

print(counter)
