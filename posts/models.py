from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	p_title = models.CharField(max_length=200)
	p_content = models.TextField(max_length=1000)
	p_date = models.DateTimeField(default=timezone.now)
	p_author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.p_title

	def get_absolute_url(self):
		return reverse('post_page', kwargs={'pk':self.pk})
