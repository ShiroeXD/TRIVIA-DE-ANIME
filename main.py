import time

import time

import random
puntaje=0
iniciar_trivia = True
intentos = 0
print("'\033[35m Un juego para tontos!'\033[39m'")
print("'\033[36m'Bienvenido a mi trivia sobre animes, es lo que mas me gusta no preguntes :V ")
print("Pondremos a prueba tus conocimientos otaku-kun.")
print("Tienes", puntaje, "puntos'\033[39m'")
nombre= input("¿Cual es tu nombre?: \n ")
print("mmm...")
time.sleep(2)
print("\n Hola", nombre,"responde las siguientes preguntas escribiendo la letra de la alternativa y presionando ´Enter´ para enviar tu respuesta: \n")
while iniciar_trivia == True: 
  intentos += 1
  puntaje = 0

  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  print('\033[32m'"1) ¿Cual es el anime donde una de las habilidades a aprender es el 'bankai'?\n ")
  print("a) Sakurasao no pet na kanoho")
  print("b) Bleach")
  print("c) Sora no otoshimono")
  print("d) My Little Pony")
  respuesta_1 = input("\n Tu respuesta: ")
  while respuesta_1 not in ("a", "b", "c", "d","aea"):
   respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_1 == "b":
    puntaje += 10
    print("Te estas luciendo", nombre, "!")
  elif respuesta_1 == "a":
     puntaje -= 10
     print("Incorrecto!", nombre, "Este anime es de comedia romance como va aver bankai mano ... nel pastel ")
  elif respuesta_1 =="d":
     puntaje -= 10
     print("Incorrecto!", nombre, "¿Es en serio? y que ¿Remboldash se pone sayayin ? ")
  else:
   print("Incorrecto", nombre, "Este anime es de comedia romance ..juiste p cavsita xD '\033[39m' ")
  time.sleep(3)
  print("'\033[33m' \n2) ¿Como se llama el personaje principal del anime City Hunter?\n")
  print("a) Kenichi Shirahama")
  print("b) Giglipop")
  print("c) Rio Saeba")
  print("d) Bad Bunny")
  respuesta_2 = input("\nTu respuesta: ")
  while respuesta_2 not in ("a", "b", "c", "d","aea"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_2 == "a":
    puntaje -= 10
    print("Incorrecto!", nombre, "Kenichi es del anime de kenichi p mano :V ")
  elif respuesta_2 == "b":
   puntaje -= 10
   print("Incorrecto!", nombre, "Giglipop nisiquiera es un anime >:V ")
  elif respuesta_2 =="d":
   puntaje -= 10
   print("Incorrecto!", nombre, "Wacala que desepción")
  else: 
   puntaje += 10
   print("Muy bien", nombre, "! '\033[39m' ")
   time.sleep(3)
  print("'\033[31m' \n3) ¿Como muere la novena en el anime de Mirai Nikki?\n")
  print("a) En la pelea con Saitama")
  print("b) la atropella camion-kun")
  print("c) Un impactrueno de Ponita")
  print("d) Hablas sonseras mano ella nunca muere :V ")
  respuesta_3 = input("\nTu respuesta: ")
  while respuesta_3 not in ("a", "b", "c", "d","aea"):
   respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_3 == "a":
    puntaje = puntaje /310
    print("Completamente Incorrecto!", nombre, "Solo a ti te mata Saitama ")
  elif respuesta_3 == "b":
    puntaje = puntaje -410
    print("Casi Incorrecto!", nombre, "Que te atropelle a ti por escoger esdta vaina mano")
  elif respuesta_3 =="c":
    puntaje = puntaje +6
    print("Incorrecto!", nombre, "Ponita tira chorro de agua sonso xD ")
  else:
    puntaje = puntaje *520
    print("Muy bien", nombre, "! '\033[39m'")
    time.sleep(2)
  print ("\nGracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos")
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  
   print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False
