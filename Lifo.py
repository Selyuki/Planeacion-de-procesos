class Lifo:
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

def lifo(procesos):
    procesos.sort(key=lambda x: x[2])  # Ordenar por llegada
    pila = []
    tiempo = 0
    completados = []

    print(f"\n{'Proceso':<10}{'Ráfaga':<8}{'Llegada':<8}{'Espera':<8}{'Retorno':<8}")

    i = 0
    while i < len(procesos) or pila:
        while i < len(procesos) and procesos[i][2] <= tiempo:
            pila.append(procesos[i])
            i += 1

        if pila:
            nombre, rafaga, llegada = pila.pop()  # Último en entrar, primero en salir
            if tiempo < llegada:
                tiempo = llegada
            espera = tiempo - llegada
            retorno = espera + rafaga
            print(f"{nombre:<10}{rafaga:<8}{llegada:<8}{espera:<8}{retorno:<8}")
            tiempo += rafaga
        else:
            tiempo += 1

if __name__ == "__main__":
    procesos = Lifo.pedir_datos()
    lifo(procesos)