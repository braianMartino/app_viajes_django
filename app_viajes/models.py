from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime as dt
import re

import logging
logger = logging.getLogger(__name__)

User= get_user_model() #U: la implementacion q este configurada

class Lugar(models.Model): #U: cualquier texto que publiquemos, despues especializamos
	de_quien= models.ForeignKey('auth.User', on_delete=models.CASCADE)
	fh_creado= models.DateTimeField(default=timezone.now)
	fh_editado= models.DateTimeField(default=timezone.now)

	nombre= models.CharField(max_length=200)
	texto= models.TextField()
	imagen= models.ImageField() 
	#VER: https://www.geeksforgeeks.org/imagefield-django-models/

	def __str__(self):
		return f'{self.nombre}'


	
