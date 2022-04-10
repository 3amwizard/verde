from django.db import models
from django.utils import timezone

# Create your models here.
MODULE_CHOICES = (('Verde People', 'Verde People'), ('Verde Fleet', 'Verde Fleet'), ('Verde Leave', 'Verde Leave'),
    ('Verde Gift Reg', 'Verde Gift Reg'), ('Verde Claims', 'Verde Claims'), ('Verde ELC', 'Verde ELC'), ('Verde Policy', 'Verde Policy'))
SIZE_CHOICES = (('1-10', '1-10'), ('11-50', '11-50'), ('51-100', '51-100'), ('101-500', '101-500'), ('501 -1000', '501-1000'),
    ('Over 1001', 'Over 1001'))

class Business(models.Model):
	date = models.DateTimeField(default=timezone.now)
	name = models.CharField(max_length=36)
	email = models.EmailField()
	company = models.CharField(max_length=72)
	service = models.CharField(max_length=72, choices=MODULE_CHOICES)
	size = models.CharField(max_length=72, choices=SIZE_CHOICES)
	message = models.CharField(max_length=1000)

	def __str__(self):
		return self.name