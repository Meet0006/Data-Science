# // Practice

dataSet = {
    "Name": "Meet",
    "Age": 22,
    "Branch": {
        "1": "Civil",
        "2": "IT",
        "3": "CE"
    },
    "CE_Branch": [
        {
            "Enroll1": 1,
            "Enroll2": 2,
        },
    ]
}
print(dataSet["Branch"].values())
print(dataSet)
print(type(dataSet))
print(dataSet["Age"])
print(dataSet["Branch"])
print(dataSet["Branch"]["3"])
print(dataSet["CE_Branch"][0])
print(dataSet['CE_Branch'][0]["Enroll2"])
print(len(dataSet))  # // Total number of keys // Output : 4
