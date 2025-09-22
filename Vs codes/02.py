class Resturant:
    """一次模拟餐馆的简单尝试"""
    def __init__(self,resturant_name,cuisine_type):
        """初始化属性name和type"""
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type


        def describe_resturant(self):
            print('f"The {self.resturant_name} is very good !"')
            print('f"Welcome to visit {self.resturant_name}"')

        def open_resturant(self):
            print('f"This is open !"')
resturant = Resturant("zaozhaung","spicy")

print(f"that is {resturant.resturant_name}")
print(f"{resturant.cuisine_type}can have many varities")

resturant.describe_resturant()
resturant.open_resturant()

print(f"that is {resturant.describe_resturant}")
print(f"{resturant.open_resturant}can have many varities")



                
            
            
        




