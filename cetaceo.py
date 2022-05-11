class Mamifero:
  def __init__(self,cantmamas,esperanzadevida):
    self.cantmamas=cantmamas
    self.esperanzadevida=esperanzadevida

  def mamar(self):
    print('esta comiendo')

  def nacer(self):
    print('nacio')

class Animalmarino:
  def __init__(self,tienebranqueas,especie):
    self.tienebranqueas=tienebranqueas
    self.especie=especie

  def nadar(self):
    print('esta nadando')

class Cetaceo(Mamifero, Animalmarino):
  def __init__(self,cantMamas, esperanzadevida, tienebranqueas,especie,notas,viveEn,peso):

    Mamifero.__init__(self,cantMamas,esperanzadevida)
    Animalmarino.__init__(self,tienebranqueas,especie)

    self.notas=notas
    self.viveEn=viveEn
    self.peso=peso

  def nacer(self):
    print('nacio')
  
  def nadar(self):
    print('nada')

  def mostrar(self):
    print(f'Este mamifero tiene esta cantidad de mamas{self.cantmamas}, con una esperanza de vida de{self.esperanzadevida}, es este caso no tiene branqueas{self.tienebranqueas}, es de la especie{self.especie},subespecie {self.notas}, viven en el{self.viveEn} y pesa {self.peso}')


ceta1=Cetaceo(2,40,'no','ballena','azul','mar',1000)
ceta1.nacer()
ceta1.mostrar()