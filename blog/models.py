from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.user')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Dades(models.Model):
	id=models.AutoField(primary_key=True)
	nom=models.CharField(max_length=50)
	cognoms=models.CharField(max_length=150)
	dni=models.CharField(max_length=9)
	data_naixament=models.DateTimeField(null=True)
	adreça=models.CharField(max_length=350)
	telefon=models.CharField(max_length=9)
	mail=models.CharField(max_length=200)
	poblacio=models.CharField(max_length=100)
	observacions=models.TextField()
	#foto=

	def __str__(self):
		return self.cognoms

class Estudis(models.Model):
	id=models.AutoField(primary_key=True)
	nom=models.CharField(max_length=30)
	data_inici=models.DateTimeField(null=True)
	data_final=models.DateTimeField(nul=True)

	def __str__(self):
		return self.nom

class Experiencia(models.Model):
	id=models.AutoField(primary_key=True)
	lloc_treball=models.CharField(max_length=150)
	data_final=models.DateTimeField(null=True)
	data_inici=models.DateTimeField(null=True)

	def __str__(self):
		return self.lloc_treball

class Idiomes (models.Model):
	id=models.AutoField(primary_key=True)
	idioma=models.CharField(max_length=30)
	titol=models.CharField(max_length=50)

	def __str__(self):
		return self.idioma
