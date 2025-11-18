class Fruit:
    def __init__(self, name:str ) -> None:
        self.name = name

    def __mul__(self, other:int ) ->str:
        return self.name * other
    
    def __len__(self)->int:
        return 0
    
    def __str__(self) ->str:
        return self.name
    
apple :Fruit =Fruit("ApplePie")
print(apple * 4)
print(apple.name)
print(apple)