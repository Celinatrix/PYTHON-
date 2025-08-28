#A
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)

#B
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)

#C
sample_dict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}
print(sample_dict["class"]["student"]["marks"]["history"])

#D
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
my_dict = dict.fromkeys(employees, defaults)
print(my_dict)

#E
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

keys = ["name", "salary"]

new_dict = {k: sample_dict[k] for k in keys}
print(new_dict)

#F
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)

print(sample_dict)

#G
sample_dict = {'a': 100, 'b': 200, 'c': 300}

print(200 in sample_dict.values())  # 1
print(500 in sample_dict.values())  # 0

#H
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)

#I
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'History': 75
}
min_key = min(sample_dict, key=sample_dict.get)
print(min_key)

#J
sample_dict = {
  'emp1': {'name': 'Jhon', 'salary': 7500},
  'emp2': {'name': 'Emma', 'salary': 8000},
  'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary'] = 8500
print(sample_dict)