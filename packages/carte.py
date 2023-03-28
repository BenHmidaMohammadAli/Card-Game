class carte():
	
	def __init__(self,symbole, value):
		self.symbole= symbole
		self.value=value
		self.img="null"

		
	def __str__(self):
		return f"carte is : {self.symbole} -> {self.value} "

	def __reper__(self):
		return f"carte is : {self.symbole} -> {self.value} "
	
	def get_symbole(self):
		return self.symbole
	
	def get_value(self):
		return self.value