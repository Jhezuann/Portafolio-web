from django.db import models

# Create your models here.

class Portafolio(models.Model):

	titulo=models.CharField(max_length=100)
	descripcion=models.CharField(max_length=500)
	imagen=models.ImageField(upload_to='Portafolio')
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name='portafolio'
		verbose_name_plural='portafolio'

	def __str__(self):
		return self.titulo