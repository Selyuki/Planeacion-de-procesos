class prioridad:
    @staticmethod
    def pedir_datos():
        n = int(input("¿Cuántos procesos vas a ingresar? "))
        procesos = []
        for i in range(n):
            nombre = input(f"Nombre del proceso {i+1}: ")
            rafaga = int(input("Ráfaga: "))
            llegada = int(input("Llegada: "))
            prioridad = int(input("Prioridad (menor número = mayor prioridad): "))
            procesos.append([nombre, rafaga, llegada, prioridad])
        return procesos

def prior(procesos):
    tiempo = 0
    completados = []
    procesos.sort(key=lambda x: x[2])  # Ordenar por llegada
    pendientes = procesos.copy()

    print(f"\n{'Proceso':<10}{'Ráfaga':<8}{'Llegada':<8}{'Prioridad':<10}{'Espera':<8}{'Retorno':<8}")

    while pendientes:
        disponibles = [p for p in pendientes if p[2] <= tiempo]
        if not disponibles:
            tiempo += 1
            continue
        # Elegir el de mayor prioridad (menor número)
        actual = min(disponibles, key=lambda x: x[3])
        pendientes.remove(actual)
        nombre, rafaga, llegada, prior = actual
        if tiempo < llegada:
            tiempo = llegada
        espera = tiempo - llegada
        retorno = espera + rafaga
        print(f"{nombre:<10}{rafaga:<8}{llegada:<8}{prioridad:<10}{espera:<8}{retorno:<8}")
        tiempo += rafaga

if __name__ == "__main__":
    procesos = prioridad.pedir_datos()
    prior(procesos)