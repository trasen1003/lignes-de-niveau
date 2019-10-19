## Fonctions importantes

def transformation(f, c):
	def g(x,y) : return f(x,y) - c
	return g
	
def verification(f, axis = 'x', value = 0, start = 0, end = 1):
	if axis == 'x':
		if f(value,start) >= 0 and f(value,end) <= 0 : return 1
		elif f(value,start) <= 0 and f(value,end) >= 0 : return 2
		else : return 0

	elif axis == 'y':
		if f(start,value) >= 0 and f(end,value) <= 0 : return 1
		elif f(start,value) <= 0 and f(end,value) >= 0 : return 2
		else : return 0

def find_seed(f, c = 0, axis = 'x', value = 0, start = 0, end = 1,  eps = 2**-26):

	""" f : fonction à tester; c : valeur de la ligne de niveau; axis : axe selon lequel on cherche la solution
	value : valeur qui va être prise sur l'axe spécifié pour être la coordonée fixe;
	start, debut : bornes de la recherche (ie : la recherche se fera entre f(start,value) et f(end,value) si axe = 'y')
	eps : écart recherché pour la dichotomie"""

	if axis != 'x' and axis != 'y' : raise ValueError ("l'axe doit être 'x' ou 'y'")

	g = transformation(f,c)

	cas = verification(f, axis, value, start, end)
	if cas == 1 :
		return dichotomie(g, axis, value, start, end, eps)
	if cas == 2 :
		return dichotomie(g, axis, value, end, start, eps)
	else : 
		return None

def dichotomie(f, axis, value, a, b, eps):
	
	"""a est la position où f est positif et b la position où f est négatif"""

	if axis == 'x':
		while abs(b-a) > eps :
			milieu = (b + a)/2
			if f(milieu,value) > 0:
				a = milieu
			else :
				b = milieu
		return (a+b)/2
	elif axis == 'y':
		while abs(b-a) > eps :
			milieu = (b + a)/2
			if f(milieu,value) > 0:
				a = milieu
			else :
				b = milieu
		return (a+b)/2

def derive(f, x0, y0):
	return (f(x0,y0+10**-4)-f(x0,y0))/(10**-4)

def find_seed_global(f, bornes_x = [0,1], bornes_y = [0,1], pas = 10**-3, eps = 2**-26, c = 0):

	""" f est la fonction à tester et c la ligne de niveau recherchée, bornes_x et bornes_y définissent le domaine
	de recherche de la graine du processus, pas définit le pas de recherche et eps la precision de la dichotomie"""

	## recherche sur l'axe y

	x_value = bornes_x[0]
	while x_value <= bornes_x[1] and find_seed(f, c, 'x', x_value, bornes_y[0], bornes_y[1], eps) == None :
		x_value += pas

	if x_value <= bornes_x[1] : ## Une graine a été trouvée
		return (x_value, find_seed(f, c, 'x', x_value, bornes_y[0], bornes_y[1], eps))

	## recherche sur l'axe x 

	y_value = bornes_y[0]
	while y_value <= bornes_y[1] and find_seed(f, c, 'y', y_value, bornes_x[0], bornes_x[1], eps) == None :
		y_value += pas

	if y_value <= bornes_y[1] : ## Une graine a été trouvée
		return (y_value, find_seed(f, c, 'y', y_value, bornes_x[0], bornes_x[1], eps))

	raise KeyError ('Recherche non aboutie')

def Propagation(f, x0, y0, eps1, eps2, c = 0):
	def g(p,q) : return f(p,q) - c
	y = y0
	x = x0 + eps1
	nb_derive = derive(g,x0,y0)
	def psi(w):
		return w - 1/nb_derive*g(x,w)
	while g(x,y)>eps2 : 
		print(y)
		y = psi(y)
	return x,y 

