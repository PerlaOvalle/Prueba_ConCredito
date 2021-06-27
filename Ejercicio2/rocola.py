class Rocola():
  prendido = False
  canciones = ["Dancing Queen", "Waterloo", "Fernando"]
  cancionIndice = 0
  estados = ("REPRODUCIENDO", "PAUSADO", "NULO")
  estado = estados[2]
  volumen = 20

  def prender(self):
    self.prendido = True
    print("La rocola esta prendida")

  def apagar(self):
    self.prendido = False
    print("La rocola se ha apagado")  

  def reproducir(self):
    self.estado = self.estados[0]
    print("Reproduciendo cancion")

  def pausar(self):
    self.estado = self.estados[1]
    print("Cancion pausada")

  def elegirCancion(self, indice):
    self.cancionIndice = indice
    print("Cancion elegida: " + str(self.canciones[indice]))

  def nextCancion(self):
    if(self.cancionIndice == len(self.canciones)- 1):
      print("No hay cancion siguiente")
    else:
      self.cancionIndice = self.cancionIndice + 1
      print("La cancion elegida es: " + str(self.canciones[self.cancionIndice]))

  def previousCancion(self):
    if(self.cancionIndice == 0):
      print("No hay cancion previa")
    else:
      self.cancionIndice = self.cancionIndice - 1
      print("La cacion elegida es: " + str(self.canciones[self.cancionIndice]))


jukebox = Rocola()
jukebox.prender()
jukebox.elegirCancion(1)
jukebox.reproducir()
jukebox.pausar()
jukebox.nextCancion()
jukebox.previousCancion()
jukebox.apagar()