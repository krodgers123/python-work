class registration:
    def __init__(self,name,reg_no,course,year):
        self.name=name
        self.reg_no=reg_no
        self.course=course
        self.year=year

    def __str__(self):
        return(f"name:{self.name} reg_no:{self.reg_no} course:{self.course} year:{self.year}")

student1=registration("Nkambwe David","S23B13/001","DIT","2023")
print(student1)    

student1=registration("Lwanga Benard","S23B14/002","BSIT","2022")
print(student1) 

student1=registration("Natukunda Jesca","S23B13/003","LAW","2021")
print(student1)    

student1=registration("Tayebwa Thomas","S23B13/004","BSCS","2020")
print(student1)    
       
        