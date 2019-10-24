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
	
	cas = verification(g, axis, value, start, end)
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
			if f(milieu,value) >= 0:
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

def derive(f, axis, x0, y0):
	if axis == 'y':
		return (f(x0,y0+10**-4)-f(x0,y0))/(10**-4)
	if axis == 'x':
		return (f(x0+10**-4,y0)-f(x0,y0))/(10**-4)

def derive_amelioree(f, axis, x0, y0):
    def d1(f,a,h):
        """dérivée de f avec un schéma d'ordre 1"""
        return (f(a+h) - f(a))/h

    def d2(f,a,h):
        """dérivée de f avec un schéma d'ordre 2"""
        return (f(a+h)-f(a-h))/(2*h)

    def dd2(f,a):
        """dérivée seconde de f en h avec des schémas d'ordre 2"""
        h = 10**(-4) 
        return (d2(f,a+h,h)-d2(f,a-h,h))/(2*h)

    def ddd2(f,a):
        """dérivée troisième de f en h avec des schémas d'ordre 2"""
        h = 10**(-4)
        return (dd2(f,a+h)-dd2(f,a-h))/(2*h)

    def d(f):
        if axis == 'y':
            g = lambda y : f(x0,y)
            a = y0
            g3 = ddd2(g,a)
            if g3 != 0:
                h = ((2**(-63)*g(a))/g3)**(1/4)
            else:
                h = 10**(-3)
            return d2(g,y0,h)
        if axis == 'x':
            g = lambda x : f(x,y0)
            a = x0
            g3 = ddd2(g,a)
            print(g(a),ddd2(g,a))
            if g3 != 0:
                h = ((2**(-63)*g(a))/g3)**(1/4)
            else:
                h = 10**(-3)
            return d2(g,x0,h)

    return d(f)


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
		return (find_seed(f, c, 'y', y_value, bornes_x[0], bornes_x[1], eps), y_value)

	return None

def Propagation(f, axis, x0, y0, eps1, eps2, c = 0):
	if axis!= 'x' and axis != 'y' : raise ValueError('Axis mal donné')
	
	def g(p,q) : return f(p,q) - c
	
	t1 = time.time()
	
	if axis == 'y' : 
		y = y0
		x = x0 + eps1
	
	if axis == 'x':
		x = x0
		y = y0 + eps1
	
	nb_derive = derive(g,axis,x0,y0)
	
	if axis == 'y':
		def psi(w):
			return w - 1/nb_derive*g(x,w)
		
		while abs(g(x,y))>eps2 and abs(y) < 10**6 and time.time()-t1 < 10**-3:
			y = psi(y)
		
		if time.time() - t1 >= 10**-3 : return x,10**7

	if axis == 'x':
		def psi(w):
			return w - 1/nb_derive*g(w,y)
		
		while abs(g(x,y))>eps2 and abs(x) < 10**6 and time.time()-t1 < 10**-3:
			x = psi(x)
		
		if time.time() - t1 >= 10**-3 : return 10**7,y
	
	return x,y 

def Jacobienne(f, x, y):
	

def Propagation2(f, x0, y0, eps1, eps2, c = 0):


def decoupe(x_lim = [0,1], y_lim = [0,1], eps = 10**-3) :
	Liste_domaine = []

	x_min, x_max = x_lim
	y_min, y_max = y_lim
	x = x_min
	while x + eps < x_max :
		y = y_min
		while y + eps < y_max :
			y_field = [y, y + eps]
			x_field = [x, x + eps]
			y += eps
			Liste_domaine.append([x_field, y_field])

		x += eps

	return Liste_domaine	
	

def ligne_niveau(f, c = 0, x_lim = [0,1], y_lim = [0,1], eps1 = 10**-3, eps2 = 2**-26):
	Liste_x = []
	Liste_y = []

	Liste_domaine = decoupe(x_lim, y_lim, eps1)
	k = 0
	for x_field, y_field in Liste_domaine:
		k += 1
		if find_seed_global(f, x_field, y_field, eps1/10, eps2, c) != None:
			x0, y0 = find_seed_global(f, x_field, y_field, eps1/10, eps2, c)
			Liste_x.append(x0)
			Liste_y.append(y0)
			x_plus = x0
			x_moins = x0
			y = y0
			while x_moins > x_field[0]:
				x_moins,y = Propagation(f, 'y', x_moins, y, - eps1/100, eps2, c)
				if abs(y) >= 10**6 : break
				Liste_x.append(x_moins)
				Liste_y.append(y)
			y = y0
			while x_plus < x_field[1]:
				x_plus,y = Propagation(f, 'y', x_plus, y, eps1/10, eps2, c)
				if abs(y) >= 10**6 : break
				Liste_x.append(x_plus)
				Liste_y.append(y)
			x = x0
			y_moins = y0
			y_plus = y0
			while y_moins > y_field[0]:
				x,y_moins = Propagation(f, 'x', x, y_moins, -eps1/10, eps2, c)
				if abs(x) >= 10**6 : break
				Liste_x.append(x)
				Liste_y.append(y_moins)
			while y_plus < y_field[1]:
				x,y_plus = Propagation(f, 'x', x, y_plus, eps1/10, eps2, c)
				if abs(x) >= 10**6 : break
				Liste_x.append(x)
				Liste_y.append(y_plus)
	return Liste_x, Liste_y

def ligne_niveau2(f, c = 0, x_lim = [0,1], y_lim = [0,1], eps1 = 10**-3, eps2 = 2**-26):
	Liste_x = []
	Liste_y = []

	Liste_domaine = decoupe(x_lim, y_lim, eps1)
	k = 0
	for x_field, y_field in Liste_domaine:
		k += 1
		if find_seed_global(f, x_field, y_field, eps1/10, eps2, c) != None:
			x, y = find_seed_global(f, x_field, y_field, eps1/10, eps2, c)
			while x_field[0] <= x and x <= x_field[1] and y_field[0] <= y and y <= y_field[1] :
				x, y = Propagation2()

def affiche_ligne(f, Liste_c = [0], x_lim = [0,1], y_lim = [0,1], eps1 = 10**-3, eps2 = 2**-26):

	plt.figure()
	plt.title(f"Lignes de niveau de f associée à {Liste_c}")
	plt.xlabel('x')
	plt.ylabel('y')
	for c in Liste_c:
		print(c)
		Liste_x,Liste_y = ligne_niveau(f, c, x_lim, y_lim, eps1, eps2)
		plt.plot(Liste_x,Liste_y, marker = '.', linestyle = ' ', label = f"{c}")
		plt.xlim(x_lim[0], x_lim[1])
		plt.ylim(y_lim[0], y_lim[1])
		plt.legend(loc=1)
	plt.show()


