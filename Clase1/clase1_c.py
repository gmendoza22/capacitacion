from clase1_a import Animal


class Gato(Animal):
    def araniar(self):
        print("Te araño")


cat = Gato("Mazapań", 2, 4)
cat.describe()
print(cat.nombre)
cat.araniar()
