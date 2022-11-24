class Autor():
    def __init__(self, id, apellidos,nombres,fechanacimiento=None):
        self.id = id
        self.apellidos = apellidos
        self.nombres = nombres
        self.fechanacimiento = fechanacimiento

    def nombre_completo(self):
        nombre_completo = self.apellidos + ", " + self.nombres
        return nombre_completo
