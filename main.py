import datetime 

def ver_dia ():
  
  dias = [
  
    "segunda",
    "terça", 
    "quarta",
    "quinta",
    "sexta",
    "sábado",
    "domingo"
  ]
  
  data = datetime.datetime.now() 
  indice = data.weekday()
  dia_semana = dias[indice]
  
  return dia_semana
    

hoje= ver_dia()
#hoje = "quinta"

if hoje in ["quarta"]:
  print("hoje é quarta feira")

else:
  print("Hoje é outro dia")