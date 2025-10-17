class SJF:
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

    @staticmethod
    def sjf(procesos):
        procesos.sort(key=lambda x: (x[2], x[1]))
        tiempo = 0
        print(f"\n{'Proceso':<10}{'Ráfaga':<8}{'Llegada':<8}{'Espera':<8}{'Retorno':<8}")
        while procesos:
            disponibles = [p for p in procesos if p[2] <= tiempo]
            if disponibles:
                proceso = min(disponibles, key=lambda x: x[1])
                procesos.remove(proceso)
                nombre, rafaga, llegada = proceso
                espera = tiempo - llegada
                retorno = espera + rafaga
                print(f"{nombre:<10}{rafaga:<8}{llegada:<8}{espera:<8}{retorno:<8}")
                tiempo += rafaga
            else:
                tiempo = min(procesos, key=lambda x: x[2])[2]

if __name__ == "__main__":
    procesos = SJF.pedir_datos()
    SJF.sjf(procesos)