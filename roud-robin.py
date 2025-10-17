class RoundRobin:
    @staticmethod
    def pedir_datos():
        n = int(input("¿Cuántos procesos vas a ingresar? "))
        quantum = int(input("Quantum: "))
        procesos = []
        for i in range(n):
            nombre = input(f"Nombre del proceso {i+1}: ")
            rafaga = int(input("Ráfaga: "))
            llegada = int(input("Llegada: "))
            prio = int(input("Prioridad (número, menor = más prioridad): "))
            procesos.append({
                'nombre': nombre,
                'rafaga': rafaga,
                'llegada': llegada,
                'restante': rafaga,
                'prio': prio
            })
        return procesos, quantum

def _insertar_por_prioridad(cola, proc):
    # inserta en cola manteniendo prioridad (menor = mayor prioridad)
    for idx, p in enumerate(cola):
        if p['prio'] > proc['prio']:
            cola.insert(idx, proc)
            return
    cola.append(proc)

def round_robin(procesos, quantum):
    tiempo = 0
    cola = []
    completados = []
    procesos.sort(key=lambda x: x['llegada'])
    i = 0

    print(f"\n{'Proceso':<10}{'Inicio':<8}{'Fin':<8}{'Prior.':<8}")

    while procesos or cola:
        # añadir procesos que llegan ahora
        while i < len(procesos) and procesos[i]['llegada'] <= tiempo:
            _insertar_por_prioridad(cola, procesos[i])
            i += 1

        if cola:
            actual = cola.pop(0)
            inicio = tiempo
            ejecucion = min(quantum, actual['restante'])
            tiempo += ejecucion
            actual['restante'] -= ejecucion
            print(f"{actual['nombre']:<10}{inicio:<8}{tiempo:<8}{actual['prio']:<8}")
            # registrar llegada de nuevos durante la ejecución
            while i < len(procesos) and procesos[i]['llegada'] <= tiempo:
                _insertar_por_prioridad(cola, procesos[i])
                i += 1
            if actual['restante'] > 0:
                _insertar_por_prioridad(cola, actual)
            else:
                actual['fin'] = tiempo
                completados.append(actual)
        else:
            # avanzar al siguiente tiempo de llegada si no hay nada en la cola
            if i < len(procesos):
                tiempo = procesos[i]['llegada']
            else:
                break

    # resumen con espera y retorno
    if completados:
        print(f"\n{'Proceso':<10}{'Llegada':<8}{'Ráfaga':<8}{'Espera':<8}{'Retorno':<8}")
        for p in completados:
            espera = p['fin'] - p['llegada'] - p['rafaga']
            retorno = p['fin'] - p['llegada']
            print(f"{p['nombre']:<10}{p['llegada']:<8}{p['rafaga']:<8}{espera:<8}{retorno:<8}")

if __name__ == "__main__":
    procesos, quantum = RoundRobin.pedir_datos()
    round_robin(procesos, quantum)