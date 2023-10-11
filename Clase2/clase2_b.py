from clase2_a import Animal

class Perro(Animal):
    pass
    def __init__(self, nombre, edad, patas, duenio):
        super(Perro, self).__init__(nombre, edad, patas) #Llama la función del padre
        self.duenio = duenio
        
    def describe(self):
        super(Perro, self).describe()
        print(f"El dueño es {self.duenio}")

dog = Perro("Bodoque", 13, 4, "Hector")
dog.describe()


