from enum import Enum

# Enum TipoInstrumento

class TipoInstrumento(Enum):
    PERCUSION = 1
    VIENTO = 2
    CUERDA = 3

# Fabrica

class Fabrica:
    def __init__(self):
        self.sucursales = []

    def porc_instrumentos_por_tipo(self, nombre_suc):
        porcentajes = [0.0] * len(TipoInstrumento)
        suc_encontrada = self.buscar_sucursal(nombre_suc)
        if suc_encontrada:
            porcentajes = suc_encontrada.porc_instrumentos_por_tipo()
        return porcentajes

    def buscar_sucursal(self, nombre_suc):
        suc_encontrada = None
        for sucursal in self.sucursales:
            if sucursal.nombre == nombre_suc:
                suc_encontrada = sucursal
                break
        return suc_encontrada

    def borrar_instrumento(self, ID):
        borrado = None
        for sucursal in self.sucursales:
            borrado = sucursal.borrar_instrumento(ID)
            if borrado:
                break
        return borrado

    def listar_instrumentos(self):
        for sucursal in self.sucursales:
            print(sucursal.nombre)
            sucursal.listar_instrumentos()

    def instrumentos_por_tipo(self, tipo):
        inst_encontrados = []
        for sucursal in self.sucursales:
            inst_encontrados.extend(sucursal.instrumentos_por_tipo(tipo))
        return inst_encontrados

    def agregar_sucursal(self, suc):
        self.sucursales.append(suc)


# - instrumento

class Instrumento:
    def __init__(self, ID, precio, tipo):
        self.ID = ID
        self.precio = precio
        self.tipo = tipo

    def get_ID(self):
        return self.ID

    def get_tipo(self):
        return self.tipo

    def __str__(self):
        return f"Instrumento{{ID={self.ID}, precio={self.precio}, tipo={self.tipo}}}"

# sucursal

class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def borrar_instrumento(self, ID):
        ins_a_borrar = self.buscar_instrumento(ID)
        self.instrumentos.remove(ins_a_borrar)
        return ins_a_borrar

    def buscar_instrumento(self, ID):
        for instrumento in self.instrumentos:
            if Instrumento.get_ID() == ID:
                return instrumento
        return None

    def porc_instrumentos_por_tipo(self):
        cant_instrumentos = len(TipoInstrumento)
        porcentajes = [0] * cant_instrumentos
        for instrumento in self.instrumentos:
            porcentajes[instrumento.get_tipo().value] += 1
        self.absoluto_a_porcentaje(porcentajes)
        return porcentajes

    def absoluto_a_porcentaje(self, porcentajes):
        total_instrumentos = len(self.instrumentos)
        for i in range(len(porcentajes)):
            porcentajes[i] = (porcentajes[i] * 100) / total_instrumentos

    def agregar_instrumento(self, ins):
        self.instrumentos.append(ins)

    def get_nombre(self):
        return self.nombre

    def listar_instrumentos(self):
        for instrumento in self.instrumentos:
            print(instrumento)

    def instrumentos_por_tipo(self, tipo):
        inst_encontrados = []
        for instrumento in self.instrumentos:
            if instrumento.get_tipo() == tipo:
                inst_encontrados.append(instrumento)
        return inst_encontrados

# MAIN - EJECUCIÓN

class Principal:
    @staticmethod
    def main():
        f = Fabrica()
        Principal.cargar_fabrica(f)

        # PRUEBA PUNTO A)
        f.listar_instrumentos()
        # PRUEBA PUNTO B)
        """ lista = f.instrumentos_por_tipo(TipoInstrumento.PERCUSION)
        for instrumento in lista:
            print(instrumento) """
        # PRUEBA PUNTO C)
        """
        borrado = f.borrar_instrumento("ZZZ111")
        print("Se borró:", borrado)
        f.listar_instrumentos()
        """
        # PRUEBA PUNTO D)
        """
        porcs = f.porc_instrumentos_por_tipo("Sasdasd")
        for porc in porcs:
            print(porc)
        """

    @staticmethod
    def cargar_fabrica(f):
        s1 = Sucursal("Sucursal A")
        s2 = Sucursal("Sucursal B")

        s1.agregar_instrumento(Instrumento("ABC123", 13214, TipoInstrumento.CUERDA))
        s1.agregar_instrumento(Instrumento("BCD456", 13432, TipoInstrumento.VIENTO))
        s1.agregar_instrumento(Instrumento("DEF567", 15464, TipoInstrumento.PERCUSION))

        s2.agregar_instrumento(Instrumento("ASD353", 52432, TipoInstrumento.CUERDA))
        s2.agregar_instrumento(Instrumento("VXCBE2", 45645, TipoInstrumento.VIENTO))
        
        Fabrica.agregar_sucursal(s1)
        Fabrica.agregar_sucursal(s2)

