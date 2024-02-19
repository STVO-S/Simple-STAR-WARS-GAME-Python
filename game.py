"""
Información que será movida al README.
Este proyecto ser creado con el fin de poner en práctica mi logica de programación usando lo aprendido hasta ahora con
Python, este proyecto será creado solo con IF, Elif, Else. Es totalmente inspirado en STAR WARS.
"""
# Introducción al juego con una breve explicación de las secuencias que veremos
print("""

               .|'''.|  |''||''|     |     '||''|.      '|| '||'  '|'     |     '||''|.    .|'''.|  
               ||..  '     ||       |||     ||   ||      '|. '|.  .'     |||     ||   ||   ||..  '  
                ''|||.     ||      |  ||    ||''|'        ||  ||  |     |  ||    ||''|'     ''|||.  
              .     '||    ||     .''''|.   ||   |.        ||| |||     .''''|.   ||   |.  .     '|| 
              |'....|'    .||.   .|.  .||. .||.  '|'        |   |     .|.  .||. .||.  '|' |'....|' 


Introducción:
Este juego trata de la toma de decisiones y como cada una de ellas van a definir si estas mas cerca de ser un Jedi, 
Sith ó Clon. Tu planeta natal sera Tatooine y la historia sera narrada en este lugar.

El sistema de juego es simple, al iniciar debes escoger a que bando crees pertenecer entre las mencionadas anteriormente
desde esta manera comenzaremos mostrándote la perspectiva de tu elección y de acuerdo a las decisiones que hayas tomado 
iras experimentando ciertos cambios en la trama como inclinarte por otro bando, desbloquear habilidades dignas 
del bando al que perteneces o te estes inclinando.

Al finalizar este juego sabras a que bando estas destinado a pertenecer, que la fuerza te acompañe.
""")

# Input para ejecutar el juego
iniciar = input("Haz click en la tecla ENTER para iniciar: ")

# Bienvenida e inicio del juego
print("""
Bienvenidos y Bienvenidas. Saludos donde sea que te encuentres en Tatooine, el dia de hoy pondremos en practica 
tus valores para descubrir a que lado perteneces. Si estas destinado a convertirte en Jedi, tal vez tu destino es 
pertenecer al lado oscuro como un Sith ó quizás eres un Clon creado para seguir ordenes, pero descuida en este dia 
vamos averiguarlo sigue lo que dice tu corazon y descubre lo que la fuerza tiene deparado para ti.

Elige a quien crees perteneces
Jedi 🟢
Sith 🔴
Clon ⚪
(Cualquier elección que difiera de las mostrada previamente dara a entender tu posición a una vida común 🟡)
""")

# Variable para la elección de bando
selection = input("Ingresa tu elección para iniciar este travesía: ")

# JEDI
if selection.lower() == "jedi":
    print("""
--INGRESAR UN LOGO JEDI--

HAZ TOMADO EL CAMINO DE LA FUERZA.
El maestro Obi-Wan Kenobi ha reconocido el esfuerzo que haz invertido en estos últimos años de entrenamiento y cree que 
ya estas listo para participar en tu primera incursion como JEDI a su lado, felicitaciones de ante mano pero cabe 
recalcar que esto no sera nada fácil y te enfrentaras a muchas decisiones complicadas, pero recuerda joven padawan 
Un JEDI no puede amar porque el amor lleva al miedo, el miedo al odio y el odio conduce al lado oscuro.

ANTES DE IR A TU PRIMERA INCURSION VAMOS A INICIAR ESCOGIENDO UN SABLE DE LUZ.
ESCOGE SABIAMENTE ENTRE:
A - SABLE DE LUZ AZUL 🔵 🟢 🟣
B - NADA ⚪
    """)
    # Selección de sable de luz
    sableDeLuz = input("Ingresa tu opción aquí: ")

    if sableDeLuz.lower() == 'a':

        # primer escenario de decisión
        print("""
Padawan te pondré al tanto de la situación que veremos en Tatooine. Los Sith han iniciado un ataque devastador arrasando
con todo a su paso y tomando como esclavos a la población de Tatooine para poder dominar esa zona de la galaxia. 
Necesitamos de tu ayuda para poder vencerlos, no sera una batalla nada sencilla sigue lo que te diga tu corazon y 
que la fuerza te acompañe.
    
Tu misión es infiltrarte en la base enemiga y con la ayuda de tu droide deshabilitar el sistema de defensa enemigo y las
compuertas donde encarcelados se encuentras los rehenes. Desconocemos a quienes tengan de rehenes, pero haz tu mejor 
trabajo para protegerlos a todos y mantente alerta ante cualquier enemigo ya que te enfrentaras a muchos.

Acabas de llegar a la zona de guerra y te das cuenta que la base enemiga esta en tu pueblo natal y te encuentras con 
un peloton de Clones comandados por los Sith. Aquí empieza todo, tienes algunas opciones para elegir:

A - Decides atacarlos y entrar a la fuerza, ya que no sera complicado para ti vencerlos a todos.
B - Prefieres llamar la atención del peloton a otro lado para entrar con cautela.
C - Llamas la atención de unos de los Clones para quitarle el traje y entrar con cautela. 
    """)

        escenario1 = input("Ingresa tu elección aquí: ")
        if escenario1.lower() == 'a':
            print("""
Ya que tienes un sable laser y un gran entrenamiento logras vencerlos a todos sin mucho problema, pero esta decision
llama la atención de muchos mas clones y terminas haciendo masacrando una gran parte de los Clones, todo ese 
desastre que causaste podría iniciar ciertos eventos que tornaran un camino totalmente diferente para ti.
        """)
        elif escenario1.lower() == 'b':
            print("""
Esta decision es inteligente de tu parte, pero los clones notan tu presencia y debes actuar de manera violenta y 
atacarlos, tratas de vencerlos sin llamar mucho la atención y entras rápidamente a la base enemiga para seguir con 
tu misión.
        """)
        elif escenario1.lower() == 'c':
            print("""
Un decision astuta, al ejecutar esta a la perfección notas que los clones son idénticos a ti y quedas en un shock
momentáneo lo cual te traerá muchas dudas, pero continuas con la misión entrando a la base enemiga.
        """)
        else:
            print("""
Tardas mucho en accionar y los clones te notan, se planifican para atacarte y logran matarte.
FIN DEL JUEGO.
""")

    else:
        print('\nNO TIENES UN SABLE DE LUZ ⚪')

        # primer escenario pero sin espada
        print("""
Padawan te pondré al tanto de la situación que veremos en Tatooine. Los Sith han iniciado un ataque devastador arrasando
con todo a su paso y tomando como esclavos a la población de Tatooine para poder dominar esa zona de la galaxia. 
Necesitamos de tu ayuda para poder vencerlos, no sera una batalla nada sencilla sigue lo que te diga tu corazon y 
que la fuerza te acompañe.
    
Tu misión es infiltrarte en la base enemiga y con la ayuda de tu droide deshabilitar el sistema de defensa enemigo y las
compuertas donde encarcelados se encuentras los rehenes. Desconocemos a quienes tengan de rehenes, pero haz tu mejor 
trabajo para protegerlos a todos y mantente alerta ante cualquier enemigo ya que te enfrentaras a muchos.

Acabas de llegar a la zona de guerra y te das cuenta que la base enemiga esta en tu pueblo natal y te encuentras con 
un peloton de Clones comandados por los Sith. Aquí empieza todo, tienes algunas opciones para elegir:

A - Decides atacarlos y entrar a la fuerza, ya que no sera complicado para ti vencerlos a todos.
B - Prefieres llamar la atención del peloton a otro lado para entrar con cautela.
C - Llamas la atención de unos de los Clones para quitarle el traje y entrar con cautela. 
    """)

        escenario1 = input("Ingresa tu elección aquí: ")
        if escenario1.lower() == 'a':
            print("""
Ya que no tienes un sable laser, pero si un gran entrenamiento logras vencer a muchos de ellos sin mucho problema, pero 
esta decision llama la atención de muchos mas clones y terminas siendo masacrado por los Clones, todo ese desastre que 
causaste te trajo la muerte.
FIN DEL JUEGO.
            """)
        elif escenario1.lower() == 'b':
            print("""
Esta decision es inteligente de tu parte, pero los clones notan tu presencia y debes actuar de manera violenta y 
atacarlos, tratas de vencerlos sin llamar mucho la atención y entras rápidamente a la base enemiga para seguir con 
tu misión al entrar notas que estas herido ya que al noter sable para defenderte te expusiste demasiado, esto podrá ser
un problema luego.
            """)
        elif escenario1.lower() == 'c':
            print("""
Un decision astuta, al ejecutar esta a la perfección notas que los clones son idénticos a ti y quedas en un shock
momentáneo lo cual te traerá muchas dudas, pero continuas con la misión entrando a la base enemiga.
        """)
        else:
            print("""
Tardas mucho en accionar y los clones te notan, se planifican para atacarte y logran matarte.
FIN DEL JUEGO.
""")


# SITH
elif selection.lower() == "sith":
    print('\nLOGO SITH')

# CLON
elif selection.lower() == "clon":
    print('\nLOGO CLON')

# CIUDADANO COMÚN
else:
    print('\nLOGO CIUDADANO COMÚN')
    print("""
Elegiste una vida común, donde vivirás en Tatooine con tu familia sin pertenecer a bando alguno.
    """)
