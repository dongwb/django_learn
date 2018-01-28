from django.db import models

class Blog(models.Model):
	"""docstring for Person"model.Modlef __init__(self, arg):
		super(Person,model.Modle.__init__()
		self.arg = arg
		
"""
	name=models.CharField(max_length=100)
	tagline=models.IntegerField()
	def __str__(self):
		return self.name
class Author(models.Model):
	"""docstring for Author"models.Modelf __init__(self, arg):
		super(Author,models.Model.__init__()
		self.arg = arg
	"""
	name=models.CharField(max_length=50)
	email=models.EmailField()
	def __str__(self):
		return self.name
class Entry(models.Model):
	"""docstring for Entry"model.Modelf __init__(self, arg):
		super(Entry,model.Model.__init__()
		self.arg = arg
	"""
	blog = models.ForeignKey(Blog)
	headline=models.CharField(max_length=255)
	body_text=models.TextField()
	pub_date=models.DateField()
	mod_date=models.DateField()
	authors=models.ManyToManyField(Author)
	n_comments=models.IntegerField()
	n_pingbacks=models.IntegerField()
	rating=models.IntegerField()

	def __str__(self):
		return self.headline
		pass