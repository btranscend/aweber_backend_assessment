# aweber_backend_assessment

crud widget rest api with django rest framework


# Doxygen
'''
For further documentation, see doxymentation directory and open index.html
'''

## download pip packages
```
pip install django
pip install djangorestframework
```
## run server
```
python manage.py runserver
```
## run tests
```
python manage.py test
```
## use postman to test endpoints
### Get all widgets 
GET     /widget
### Add widget               
POST    /widget/add
### Get single widget         
GET     /widget/{id}
### Update single widget     
PUT     /widget/{id}/update
### Delete single widget      
DELETE  /widget/{id}/delete


## to add test data 
```
python manage.py shell
```
### use ORM commands to add data
```
from django.db import models

widget = Widgets(name="widget_test_data", number_of_parts=5)

widget.save()
```
