# DOCUMENTATION
# installation django
-pip install django

# run django
-python manage.py runserver

# tester app
-postman

# checkbyid
	type = url
	method = 'GET'
	responetype = JSON
	responecode = 200,400,500
	url = /coba/<id>
	exampleurl = http://127.0.0.1:8000/coba/123 

	Value benar = 123 selain itu akan salah
	
	


# checkbyfile
	type = formdata
	parameter = 'document'
	method = 'POST'
	responetype = JSON
	responecode = 200,400,500
	url = /coba/
	exampleurl = http://127.0.0.1:8000/coba/ 
	
	