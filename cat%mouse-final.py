
# programa con ambos minimax funcionando pero sin aparente inteligencia 

board = [[" " for _ in range(5)] for _ in range(5)] # lista de 5 listas de 5 elementos (5x5)
#ubicacion inicial de gato y raton
cat_pos = (0, 0)  # esq sup izq
rat_pos = (4, 4)  # esq inf der
#imprime al gato y al raton en sus posciones
board[cat_pos[0]][cat_pos[1]] = "G"  # G de "Gato"
board[rat_pos[0]][rat_pos[1]] = "R" # R de "Raton"
#variables del fujo del juego
game_running = True
turns = 0
max_turns = 20
player = "G"


def print_board(board): #funcion para imprimir el tablero de forma ordenada 
    print(" +-------------------+")
    for row in board:
        print(" | " + " | ".join(row) + " | ")
        print(" +---+---+---+---+---+")

#funcion que retorna la distancia manhattan(calcula la distancia total entre dos puntos)
def manhattan(a, b):
    return abs(a[0] -b[0]) + abs(a[1] - b[1])

#funciones que evaluan el estado de juego desde cada perspectiva de cada jugador
def evaluate_rat(cat_pos, rat_pos, turns): #perspectiva Raton 

    if cat_pos == rat_pos:
        return -1000 #resta si el gato atrapa al raton
    if turns >= max_turns:
        return 1000 #suma si se llegaa l limite de turnos
    
    distance = manhattan(cat_pos, rat_pos) 
    escape_routes = len(possible_moves(rat_pos)) 
    return distance * 10 + escape_routes * 2 

def evaluate_cat(cat_pos, rat_pos, turns):

    if cat_pos == rat_pos:
        return 1000 #suma si el gato atrapa al raton
    if turns >= max_turns:
        return -1000 #resta si se llega al maximo de turnos
    
    distance = manhattan(cat_pos, rat_pos) #guardamos la distancia manhattan 
    rat_escape_routes = len(possible_moves(rat_pos)) #caminos de escape del raton
    return -distance * 10 - rat_escape_routes * 2 

#funcion de posiciones validas dentro del tablero, las almacena en una lista
def possible_moves(pos):
    i, j = pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #movimientos posibles 
    moves = []

    for di, dj in directions:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < 5 and 0 <= new_j < 5:
            moves.append((new_i, new_j))
    return moves

# funcion minimax del raton
def minimax_rat(cat_pos, rat_pos, turns, depth, is_maximizing):
    if cat_pos == rat_pos or turns >= max_turns or depth == 0: 
        return evaluate_rat(cat_pos, rat_pos, turns)    

    if is_maximizing: #maximiza (turno raton)
        best = -float("inf")
        for move in possible_moves(rat_pos):
            if move != cat_pos:
                score = minimax_rat(cat_pos, move, turns + 1, depth - 1, False)
                best = max(best, score)
        return best
    else: # minimiza (turno gato)
        best = float("inf") 
        for move in possible_moves(cat_pos):
            if move != rat_pos:
                score = minimax_rat(move, rat_pos, turns + 1, depth - 1, True)
                best = min(best, score)
        return best

def best_move_rat(cat_pos, rat_pos, turns, depth): # la funcion encargada de utilizar el minimax con los posibles mivimientos para el raton
    best_value = -float("inf")
    best_action = rat_pos

    for move in possible_moves(rat_pos): #posibles movimientos del raton
        if move != cat_pos:
            score = minimax_cat(cat_pos, move, turns + 1, depth - 1, False)
            if score > best_value:
                best_value = score
                best_action = move
    return best_action
#minimax para el gato 
def minimax_cat(cat_pos, rat_pos, turns, depth, is_maximizing):  
    if cat_pos == rat_pos or turns >= max_turns or depth == 0:
        return evaluate_cat(cat_pos, rat_pos, turns)
    
    if is_maximizing: #maximiza (turno gato)
        best = -float("inf")
        for move in possible_moves(cat_pos): 
            if move != rat_pos: 
                score = minimax_cat(move, rat_pos, turns + 1, depth - 1, False)
                best = max(best, score)
        return best
    else: #minimiza (turno raton)
        best = float("inf")
        for move in possible_moves(rat_pos):
            if move != cat_pos:
                score = minimax_rat(cat_pos, move, turns + 1, depth - 1, True)
                best = min(best, score)
        return best

def best_move_cat(cat_pos, rat_pos, turns, depth): # la funcion encargada de utilizar el minimax con los posibles mivimientos para el gato
    best_value = float("inf")
    best_action = cat_pos

    for move in possible_moves(cat_pos): #posibles movimientos del gato 
        if move != rat_pos:
            score = minimax_cat(move, rat_pos, turns + 1, depth - 1, False) 
            if score < best_value:
                best_value = score
                best_action = move
    return best_action

#bucle principal del juego
while game_running:
    print(f"El gato (G) tiene que atrapar al raton (R) antes que llegue a la cantidad maxima de turnos ({max_turns})")
    print_board(board)
    print(f"Turno de del jugador : {'Gato (G)' if player == 'G' else 'Ratón (R)'}")


    if player == "C":
        board[cat_pos[0]][cat_pos[1]] = " " #elimina la posicion actual del gato
        cat_pos = best_move_cat(cat_pos, rat_pos, turns, depth=8)#busca la mejor poscision 
        board[cat_pos[0]][cat_pos[1]] = "G" #actualiza la nueva posicion
    else:
        board[rat_pos[0]][rat_pos[1]] = " " #elimina la posicion actual
        rat_pos = best_move_rat(cat_pos, rat_pos, turns, depth=8)#busca la mejor poscision 
        board[rat_pos[0]][rat_pos[1]] = "R" #actualiza la nueva poscision

    #agrega un turno por cada vuelta
    if player == "M":
        turns += 1


    print(f"Turno N°{turns}") 

    #condiciones para terminar el bucle del juego/simulacion
    if cat_pos == rat_pos:
        print_board(board)
        print("¡El gato atrapó al ratón!")
        break
    if turns == max_turns:
        print_board(board)
        print("¡El ratón ha escapado!")
        break
        #cambia de jugador 
    player = "R" if player == "G" else "G"
