class Asiento:
    def __init__ (self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, newColor):
        if newColor == "rojo" or newColor == "verde" or newColor == "amarillo" or newColor == "negro" or newColor == "blanco":
              self.color = newColor

class Auto:
    cantidadCreados = 0
    def __init__ (self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        a = 0
        for e in self.asientos:
            if type(self.asientos[e]) == Asiento:    
                a += 1
        return a

    def verificarIntegridad(self):
        if self.motor.registro != self.registro:
            return "Las piezas no son originales"
        else:
            for e in self.asientos:
                if type(self.asientos[e]) == Asiento and self.asientos[e].registro != self.registro:
                    return "Las piezas no son originales"
            return "Auto original"

class Motor:
    def __init__ (self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, newRegistro):
        self.registro = newRegistro
    
    def asignarTipo(self, Tipo):
        if Tipo == "electrico" or Tipo == "gasolina":
            self.tipo = Tipo