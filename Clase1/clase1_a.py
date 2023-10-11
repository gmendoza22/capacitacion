class Animal:
    def __init__(self, nombre, edad, patas):
        self.nombre = nombre
        self.edad = edad
        self.patas = patas
        
    def  describe(self):
        print("Tengo {} patas".format(self.patas))
        #print("Me llamo  {} y tengo {} años".format(self.nombre, self.edad))
        print(f"Me llamo  {self.nombre} y tengo {self.patas} años".format(self.nombre, self.edad))
        