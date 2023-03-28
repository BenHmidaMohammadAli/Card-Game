class game ():
	
	def __init__(self, list_gamers, score_max,niveau ):

		self.list_gamers = list_gamers
		self.list_carte_louta= []
		self.score_max = score_max
		self.niveau = niveau

	def __str__(self):
		return f"Game  : list gamers : {self.list_gamers} liste Carta louta : {self.list_carte_louta}  score = {self.score_max} niveau = {self.niveau}"
	
	def __reper__(self):
		return f"Game  : {self.list_gamers} -> {self.list_carte_louta}  score = {self.score_max} niveau = {self.niveau}"
	
	def set_listgamers(self, list_gamers):
		self.list_gamers=list_gamers

	def set_list_carte_louta(self, list_carte_louta):
		self.list_carte_louta=list_carte_louta

	def set_score_max(self, score_max):
		self.score_max=score_max

	def set_niveau(self, niveau):
		self.niveau=niveau
	#--
	def get_listgamers(self):
		return self.list_gamers

	def get_list_carte_louta(self):
		return self.list_carte_louta

	def get_score_max(self ):
		return self.score_max

	def get_niveau(self):
		return self.niveau