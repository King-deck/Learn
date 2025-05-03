import random

class Barco:
    def __init__(self, eslora):
        self.eslora = eslora
        self.posiciones = []
        self.hundido = False

    def colocar_barco(self, fila, columna, orientacion, tablero):
        """Coloca el barco en el tablero según su orientación (horizontal/vertical)."""
        celdas = []
        for i in range(self.eslora):
            if orientacion == 'horizontal':
                celdas.append((fila, columna + i))
            else:
                celdas.append((fila + i, columna))
        
        # Verifica si las celdas están libres y dentro del tablero
        for f, c in celdas:
            if f >= 10 or c >= 10 or tablero[f][c] != ' ':
                return False
        
        # Coloca el barco
        for f, c in celdas:
            tablero[f][c] = 'B'
            self.posiciones.append((f, c))
        return True

class Tablero:
    def __init__(self):
        self.tablero = [[' ' for _ in range(10)] for _ in range(10)]
        self.barcos = []
    
    def colocar_barcos_aleatorios(self):
        """Coloca barcos aleatoriamente en el tablero."""
        esloras = [5, 4, 3, 3, 2]  # Tipos de barcos
        for eslora in esloras:
            barco = Barco(eslora)
            colocado = False
            while not colocado:
                fila = random.randint(0, 9)
                columna = random.randint(0, 9)
                orientacion = random.choice(['horizontal', 'vertical'])
                colocado = barco.colocar_barco(fila, columna, orientacion, self.tablero)
            self.barcos.append(barco)
    
    def imprimir_tablero(self, mostrar_barcos=False):
        """Muestra el tablero (con o sin barcos)."""
        print("  " + " ".join([str(i) for i in range(10)]))
        for i, fila in enumerate(self.tablero):
            fila_visible = []
            for celda in fila:
                if celda == 'B' and not mostrar_barcos:
                    fila_visible.append(' ')
                else:
                    fila_visible.append(celda)
            print(f"{i} " + " ".join(fila_visible))

    def disparar(self, fila, columna):
        """Realiza un disparo y devuelve el resultado (agua, impacto, hundido)."""
        if fila < 0 or fila >= 10 or columna < 0 or columna >= 10:
            return "Fuera del tablero"
        
        if self.tablero[fila][columna] == ' ':
            self.tablero[fila][columna] = '~'
            return "Agua"
        elif self.tablero[fila][columna] == 'B':
            self.tablero[fila][columna] = 'X'
            for barco in self.barcos:
                if (fila, columna) in barco.posiciones:
                    barco.posiciones.remove((fila, columna))
                    if not barco.posiciones:
                        barco.hundido = True
                        return "¡Barco hundido!"
                    return "¡Impacto!"
        else:
            return "Ya disparaste aquí"

def juego_batalla_naval():
    """Función principal del juego."""
    print("¡Bienvenido a Batalla Naval!")
    print("Dispara coordenadas (fila y columna, del 0 al 9).")
    
    tablero_jugador = Tablero()
    tablero_maquina = Tablero()
    
    tablero_jugador.colocar_barcos_aleatorios()
    tablero_maquina.colocar_barcos_aleatorios()
    
    while True:
        print("\n--- Tu turno ---")
        print("Tablero de la Máquina:")
        tablero_maquina.imprimir_tablero()
        
        try:
            fila = int(input("Fila (0-9): "))
            columna = int(input("Columna (0-9): "))
            resultado = tablero_maquina.disparar(fila, columna)
            print(resultado)
            
            # Verifica si la máquina perdió
            if all(barco.hundido for barco in tablero_maquina.barcos):
                print("¡Ganaste! Hundiste todos los barcos.")
                break
            
            # Turno de la máquina
            print("\n--- Turno de la Máquina ---")
            fila_maq = random.randint(0, 9)
            columna_maq = random.randint(0, 9)
            resultado_maq = tablero_jugador.disparar(fila_maq, columna_maq)
            print(f"La máquina disparó en ({fila_maq}, {columna_maq}): {resultado_maq}")
            
            # Verifica si el jugador perdió
            if all(barco.hundido for barco in tablero_jugador.barcos):
                print("¡Perdiste! La máquina hundió todos tus barcos.")
                break
            
        except ValueError:
            print("¡Coordenadas inválidas! Usa números del 0 al 9.")

if __name__ == "__main__":
    juego_batalla_naval()