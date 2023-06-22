import random
class Juego:
    def __init__(self):
        self.piedra= 1
        self.papel= 2
        self.tijera= 3
        self.jugada= 0
        self.puntaje= 0
        self.jugada_maquina= 0
        self.puntaje_maquina= 0
        
    def set_jugada(self, jugada):
        self.jugada= jugada
       
    def get_jugada(self):
        return self.jugada

    def set_puntaje(self, puntaje):
        self.puntaje= puntaje
       
    def get_puntaje(self):
        return self.puntaje 

    def set_jugada_maquina(self, jugada_maquina):
        self.jugada_maquina= jugada_maquina
       
    def get_jugada_maquina(self):
        return self.jugada_maquina

    def set_puntaje_maquina(self, puntaje_maquina):
        self.puntaje_maquina= puntaje_maquina
       
    def get_puntaje_maquina(self):
        return self.puntaje_maquina
                   
    def Q_iniciar_juego(self):
        q= input("¿Iniciar match? s/n: ")
        if q == "s":
            return True
        if q == "n":
            return False

    def mostrar_menu(self):
        menu= '''JUGADAS:
        1. Piedra
        2. Papel
        3. Tijera'''
        print(menu)
        
    def ingresar_jugada(self):
        self.mostrar_menu()
        jugada = int(input("INGRESE SU JUGADA: "))
        self.set_jugada(jugada)
        
    def generar_jugada_artificial(self):
        self.set_jugada_maquina(random.randint(1,3))
    
    def sumar_victoria_jugador(self):
        self.set_puntaje(self.get_puntaje() + 2)
    
    def sumar_victoria_maquina(self):
        self.set_puntaje_maquina(self.get_puntaje_maquina() + 2)
    
    def sumar_empate(self):
        self.set_puntaje(self.get_puntaje() + 1)
        self.set_puntaje_maquina(self.get_puntaje_maquina() + 1)

    def procesar_jugada(self,user):
        if self.get_jugada() == 1 and self.get_jugada_maquina() == 1:
            print(user+": Piedra | Software: Piedra\n¡EMPATE!")
            self.sumar_empate()
        if self.get_jugada() == 2 and self.get_jugada_maquina() == 1:
            print(user+": Papel | Software: Piedra\n¡GANA", user+"!")
            self.sumar_victoria_jugador()
        if self.get_jugada() == 3 and self.get_jugada_maquina() == 1:
            print(user+": Tijera | Software: Piedra\n¡GANA EL SOFTWARE!")
            self.sumar_victoria_maquina()

        if self.get_jugada() == 1 and self.get_jugada_maquina() == 2:
            print(user+": Piedra | Software: Papel\n¡GANA EL SOFTWARE!")
            self.sumar_victoria_maquina()
        if self.get_jugada() == 2 and self.get_jugada_maquina() == 2:
            print(user+": Papel | Software: Papel\n¡EMPATE!")
            self.sumar_empate()
        if self.get_jugada() == 3 and self.get_jugada_maquina() == 2:
            print(user+": Tijera | Software: Papel\n¡GANA", user+"!")
            self.sumar_victoria_jugador()

        if self.get_jugada() == 1 and self.get_jugada_maquina() == 3:
            print(user+": Piedra | Software: Tijera\n¡GANA", user+"!")
            self.sumar_victoria_jugador()
        if self.get_jugada() == 2 and self.get_jugada_maquina() == 3:
            print(user+": Papel | Software: Tijera\n¡GANA EL SOFTWARE!")
            self.sumar_victoria_maquina()
        if self.get_jugada() == 3 and self.get_jugada_maquina() == 3:
            print(user+": Tijera | Software: Tijera\n¡EMPATE!")
            self.sumar_empate()

    def resetear_scores(self):
        self.set_puntaje(0)
        self.set_puntaje_maquina(0)

    def asignar_victoria(self):
        if self.get_puntaje() > self.get_puntaje_maquina():
            return "(especie: humano) derrotó violentamente a la máquina!"
        if self.get_puntaje() < self.get_puntaje_maquina():
            return "fue usado cual escoba por el software para barrer el suelo!"
        if self.get_puntaje() == self.get_puntaje_maquina():
            return "tiene al azar de su lado tanto como lo tiene su contrincante de índole artificial!"
           
#main
juego0000= Juego()
jugadores= []
on= juego0000.Q_iniciar_juego()
while on == True:
    user= input("Nombre de usuario: ")
    for i in range(3):
        print("\nRONDA",i+1)
        juego0000.ingresar_jugada()
        juego0000.generar_jugada_artificial()
        juego0000.procesar_jugada(user)
    puntaje= juego0000.get_puntaje()
    victoria= juego0000.asignar_victoria()
    jugada= [user,puntaje,victoria]
    jugadores.append(jugada)
    juego0000.resetear_scores()
    on= juego0000.Q_iniciar_juego()
print("\n Puntaje | Jugador + estado")
for jugador in jugadores:
    print("   ",jugador[1], "   |","¡"+jugador[0],jugador[2])
print("¡Gracias por utilizar el software!")