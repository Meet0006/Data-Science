# PROGRAM 1 :

mydata4 = {
    "maharashtra": {
        "mumbai": {"city": "metro city", "metro": "yes"},
        "population": "20 cr"},
    "gujarat": ["AHMEDABAD", "SURAT", "RAJKOT"],
    "rajasthan": ["AJMER", "JAISALMER", {"capital": "jaipur"}, ["MEWAD", "RJ", "INR"]]
}

# Question 1 : print metro city
# Question 2 : print jaipur
# Question 3 : print Rajkot
# Question 4 : print RJ

# Subkey
print(mydata4["maharashtra"].keys())

# Question 1 : print metro city
print(mydata4["maharashtra"]["mumbai"]["city"])

# Question 2 : print jaipur
print(mydata4["rajasthan"][2]["capital"])

# Question 3 : print Rajkot
print(mydata4["gujarat"][2])

# Question 4 : print RJ
print(mydata4["rajasthan"][3][1])
