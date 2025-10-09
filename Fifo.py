class Fifo:
    tabla = []

    @staticmethod
    def pedir_datos():
        n = int(input("¿Cuántos procesos vas a ingresar? "))
        procesos = []
        for i in range(n):
            nombre = input(f"Nombre del proceso {i+1}: ")
            rafaga = int(input("Ráfaga: "))
            llegada = int(input("Llegada: "))
            procesos.append([nombre, rafaga, llegada])
        return procesos

def fifo(procesos):
    procesos.sort(key=lambda x: x[2])
    tiempo = 0
    print(f"\n{'Proceso':<10}{'Ráfaga':<8}{'Llegada':<8}{'Espera':<8}{'Retorno':<8}")
    for nombre, rafaga, llegada in procesos:
        if tiempo < llegada:
            tiempo = llegada
        espera = tiempo - llegada
        retorno = espera + rafaga
        print(f"{nombre:<10}{rafaga:<8}{llegada:<8}{espera:<8}{retorno:<8}")
        tiempo += rafaga

if __name__ == "__main__":
    procesos = Fifo.pedir_datos()
    fifo(procesos)