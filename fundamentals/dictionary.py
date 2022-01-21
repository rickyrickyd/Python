
car_dict = {
        "brand": "Ford",			# Key: Value
        "model": "Mustang",
        "year": 1964
    }

def first():

    print(car_dict)
    print(car_dict["model"])			# Try the key doesn’t exist
    print(car_dict.get("model"))		# Try the key doesn’t exist
    print(len(car_dict))
    if "model" in car_dict:
        print("Yes, 'model' is in the car_dict dictionary")
def second():
    car_dict["seats"] = 5

    # Modify year, if “year” is exist 
    car_dict["year"] = 2018

    print(car_dict) 
def third():
    # Remove specific item
    car_dist.pop("model")
    del car_dict["model"]

    # Removes the last inserted item
    car_dist.popitem()

    # Delete dictionary completely
    car_dict.clear()	
    del car_dict
def fourth():
    for key in car_dict:
        print(key)
        print(car_dict[key])

    for value in car_dict.values():
        print(value)

    for key, value in car_dict.items():
        print(key, value)	



def five():        
    my_family = {
        "child_1": {
            "name": "Anne",
            "birth_year": 2004,
            "allergy": False
        },
        "child_2": {
            "name": "Alex",
            "birth_year": 2007
        },
        "child_3": {
            "name": "John",
            "birth_year": 2011
        }
    }	

    print("\nMy Family\n")
    
    
    for family in my_family:
        for key in family:
            print(key, ":", family[key])
        
    
def six():
    for key in sorted(car_dict):
        print(key)
        print(car_dict[key])


five()