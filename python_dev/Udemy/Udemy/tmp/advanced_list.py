""" nums = [1,3,4,7,8,9]
print(nums.index(7))
del nums[2]
print (nums)
nums.insert(1, 10)
print(nums)
nums.insert(2,[33,44,22])
print(nums)
nums2 = [x**2 for x in range(10) if x%2 == 0]
print(nums2)
 """

class Employee:
    #Common class base for all employees
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1
    def displayCount(self):
        print("Total Employee %d " % Employee.empCount)
    def dispalayEmployee(self):
        print("Name : ",self.name,", Salary: ",self.salary)
emp1 = Employee("Greg",5000)
emp2 = Employee("Chris",7000)
emp1.dispalayEmployee()
emp2.dispalayEmployee()
print("Total Employee : ", Employee.empCount)



