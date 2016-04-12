import json

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]


def returnOne(name):
	for item in range(0,len(languages)):
		if languages[item]['name'] == name:
			print languages[item]['name']
			break
		else: 
			print "No existe"

print len(languages)
resultado = returnOne("Python")
resultado = returnOne("perez gadin")
resultado = returnOne("JavaScript")

