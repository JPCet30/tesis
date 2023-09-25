from moodle import Moodle
import json, time
from io import StringIO
from html.parser import HTMLParser

# Moodle

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_starttag(self, tag, attrs):
        #print("Tag de inicio:", tag)
        if tag == 'img':
          for a in attrs:
            if a[0] == 'src':
              self.imageUrl = a[1]
              self.text.write("image: "+self.imageUrl) #usamos image: para que sea compatible con rasa
              #print(self.imageUrl)

        if tag == 'a':
          for ind in attrs:
            if ind[0] == 'href':
              self.enlace = ind[1]
              self.text.write(self.enlace+" ")
              

        if tag == 'p':
          #print("Tag de inicio:", tag)
          self.text.write(".....\n\n")

            
    
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

# función para realizar strip de html
def strip_tags(html):
    s = MLStripper() # usamos esta clase para obtener el resultado
    s.feed(html)
    return s.get_data()


#import pdb # SIRVE PARA HACER DEBUGGER ESTE DEBUGGER TIENE UNA LINEA INTERACTIVA
# SE PUEDE USAR LOS COMANDOS h (help) s (step) n (next) r (return) c(continue) l (list) p Evalúa la expresión pasada como parámetro, la evalua en el contexto actual e imprime su valor.
# q (quit) 
url = 'https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php'
token = '4431b64009b3deae1dd8ac6d5a214c1a'
moodle = Moodle(url, token)
#raw_site_info = moodle('core_webservice_get_site_info')
#site_info = moodle.core.webservice.get_site_info()  # return typed site_info
#print(site_info)
#list1 = [2021, 1, 2]
argumentos = {
  "year": 2021,
  "month": 2,
  "courseid": 2,
  "includenavigation": 0

}
#raw_site_info = moodle('core_calendar_get_calendar_monthly_view',**argumentos)

def calendario_mensual():
  text = "es un texto"
  return text

print(calendario_mensual())

no_valido = {"defaulteventcontext","larrow","rarrow","nextperiodname","nextperiodlink","previousperiodname","previousperiodlink",
"'weekday","previousperiod","initialeventsloaded","nextperiod","includenavigation","periodname","date","view",
"daynames","filter_selector","categoryid","courseid","url"
}

no_valido_dia = {"prepadding","postpadding"}

"""
for x in raw_site_info:
  if x not in no_valido:
    #print(raw_site_info[x][1].items())
    cantidad_semanas = len(raw_site_info[x])
    print(cantidad_semanas)
    # SEMANA
    for k, v in raw_site_info[x][3].items():
      if k not in no_valido_dia:
        #print(len(k),"\n")
        # DIA DE LA SEMANA
        for tipo in range(len(v)):
          for k,vv in v[tipo].items():
            #print("")
            print(k,"---",vv)
"""

# OBTENEMOS LOS EVENTOS DE UN CURSO DEFINIDOS EN UN CALENDARIO
# FUNCIONA
"""
for semana in raw_site_info['weeks']:
  for dia in semana['days']:
    print(dia['daytitle'],"\n\n")
    for evento in dia['events']:
      print(time.ctime(evento['timestart']),"\n\n")
"""
#OBTENEMOS LAS PÁGINAS DE UN CURSO
argumentos2 = {
  "courseids": [2]
}
paginas = moodle('mod_page_get_pages_by_courses',**argumentos2)

"""
# DEVUELVE ID DE LA PÁGINA DEL CURSO
for pagina in paginas['pages']:
  print(pagina['id']," ",pagina['name'],"\n\n") # USAMOS coursemodule DEL MÓDULO DE LA PAGE para construir URL
"""



for pagina in paginas['pages']:
  if pagina['coursemodule'] == 53:
    print(pagina['name']," --> ",pagina['coursemodule'],"\n")
  else:
    print("Sin contenido")
  # con strip_tags eliminamos las etiquetas HTML
  #print(strip_tags(pagina['intro'])," --> ",strip_tags(pagina['content']),"\n")


#print(paginas)
#OBTENEMOS EL CONTENIDO DE UN PÁGINA


argumentos3 = {
  'pageid': 11
}

contenidos = moodle.mod.page.view_page(pageid=3)

#print(contenidos)





"""
nuevo = {k: raw_site_info[k] for k in raw_site_info.keys() - no_valido}


for llave,valor in nuevo.items():
  cantidad_semanas = len(valor)
  for tipo in range(len(valor)):
    #print(type(llave))
    for k,dias in valor[tipo].items():
      if k not in no_valido_dia:
        for dia in range(len(dias)):
          print(" --- ",dia,"\n\n")

"""

  #print(llave,' - ',len(valor))





#print(nuevo)


#pdb.set_trace() # HACE TRACER DL DEBUGGER
#info = json.loads(raw_site_info) 
#print(raw_site_info['weeks'])


class A:
  def m(x,y):
    print("es un test")

    return x+y


class B:
  def a():
    r = A.m(2,1)
    print(r)

B.a()