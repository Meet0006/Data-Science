# PROGRAM 2 :

mydata5 = {
    "category": [
        {
            "A": "FIRST",
            "package": {"data": "2lacs"}},
        {"B": "Second", "data": {"new": [100]}},
        {"C": "Third", "Tests": [45, 75, 25]}
    ]
}

# Question 1 : print 2lacs
# Question 2 : print 25
# Question 3 : print 100

# Question 1 : print 2lacs
print(mydata5["category"][0]["package"]["data"])

# Question 2 : print 25
print(mydata5["category"][2]["Tests"][2])

# Question 3 : print 100
print(mydata5["category"][1]["data"]["new"][0])
