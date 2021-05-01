# Taschenrechner
while True:
  num1 = input("Gib die erste Zahl ein: ")
  num11 = input("gib deine erste Zahl nach dem Komma ein: ")
  oper = input("Welche Rechenoperation soll durchgefuehrt werden? (+,-,/.,*): ")
  num2 = input("Gib die zweite Zahl ein: ")
  num21 = input("Gib deine zweite Zahl nach dem Komma ein: ")
  
  numA = float(str(num1) + "." + str(num11))
  numB = float(str(num2) + "." + str(num21))
  
  if (oper == "+"):
    print("Deine Rechnung:", numA, " + ", numB)
    print("Ergebnis:", numA + numB)
    
  elif(oper == "-"):
     print("Deine Rechnung:", numA, " - ", numB)
     print("Ergebnis:", numA - numB)
    
  elif(oper == "/"):
     print("Deine Rechnung:", numA, " / ", numB)
     print("Ergebnis:", numA / numB)

  elif(oper == "*"):
     print("Deine Rechnung:", numA, " * ", numB)
     print("Ergebnis:", numA * numB)
  else:
     print("Deine Eingaben sind nicht gueltig")

  jein = input("Willst du weiter rechnen? (ja/nein)")

  if jein == "ja":
     print("Das isch ja mega he. Nächste rechnung bitte!")
  
  else:
    print("Ok tschüss du kaspar")
    quit()
