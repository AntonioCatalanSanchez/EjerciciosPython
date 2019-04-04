import re

print "-------------VALIDAR CORREO---------------"
email="antoniocs1988@gmail.com"

def validarcorreo(email):


    if re.search("[^A-Z|a-z]+[@]+[a-z]", email) and (re.search(".com$", email) or re.search(".es$",email)):
        print("correo valido")
    else:
        print "correo mal escrito"

validarcorreo(email)


print "-------------VALIDAR URL---------------"

patron = re.compile(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$")
url="www.google.es"

def validarurl(url):

    if re.search("^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$", url):
        print "url correcta"
        print url
    else:
        print "url incorrecta"

validarurl(url)
