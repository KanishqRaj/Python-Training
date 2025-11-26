student = {
    "name" : "Kanishq",
    "age" : 22,
    "dept" : "ECE"
}

print(student["name"])
print(student.get("age"))

student["age"] = 23
student["city"] = "COIMBATORE"
print(student)

student.pop("city")
del student["dept"]
print(student)