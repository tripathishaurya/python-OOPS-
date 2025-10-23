class employee:
    #special method/magic method/dunder method -constructor
    def __init__(self):
        print("started executing attributes /data")
        self.id =123
        self.salary =50000
        self.designation="sde"
        print("ending executing attributes /data")

    def travel(self,destination):
        print("this travel function was called manually")
        print(f"EMPLOYEE is now travelling to {destination}")



# creating the instance of the class
sam=employee()

#print(sam.salary)
sam.travel("banglore")
print(type(sam))