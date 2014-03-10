
## Comenzando con Python ...

#### Tipos y operaciones

###### Números

# In[1]:

mi_numero = 9
mi_otro_numero = 5.54
print type(mi_numero), type(mi_otro_numero)


# Out[1]:

#     <type 'int'> <type 'float'>
# 

# In[2]:

mi_numero * 4 + mi_otro_numero


# Out[2]:

#     41.54

# In[3]:

mi_numero / 2


# Out[3]:

#     4

# In[4]:

mi_numero / 2.0


# Out[4]:

#     4.5

# In[5]:

from __future__ import division
mi_numero / 2


# Out[5]:

#     4.5

# In[6]:

_4 ** 2


# Out[6]:

#     20.25

# In[ ]:

2 + 3j


# In[7]:

_6 + (1 + 1j)


# Out[7]:

#     (21.25+1j)

# In[8]:

1j ** 2


# Out[8]:

#     (-1+0j)

###### Booleanos

# In[9]:

esto_es_verdadero = True


# In[10]:

esto_es_falso = False


# In[11]:

not esto_es_verdadero


# Out[11]:

#     False

# In[12]:

esto_es_verdadero and not esto_es_falso


# Out[12]:

#     True

###### Conversiones

# In[13]:

int(_8)


# Out[13]:


    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    <ipython-input-13-5f04aee87215> in <module>()
    ----> 1 int(_8)
    

    TypeError: can't convert complex to int


# In[14]:

int(10.23455)


# Out[14]:

#     10

# In[15]:

float(_)


# Out[15]:

#     10.0

# In[16]:

complex(_)


# Out[16]:

#     (10+0j)

###### Cadenas

# In[17]:

mi_cadena = 'mi primer cadena'
otra_cadena = "hola mundo"
cadena_multili = """Esta es una cadena
de varias lineas
!:)"""
print cadena_multili
print mi_cadena


# Out[17]:

#     Esta es una cadena
#     de varias lineas
#     !:)
#     mi primer cadena
# 

# In[18]:

mi_cadena + ' es ' + otra_cadena


# Out[18]:

#     'mi primer cadena es hola mundo'

# In[26]:

mi_cadena + ' ' * 4 +'\n ' +  mi_cadena*2  


# Out[26]:

#     'mi primer cadena    \n mi primer cadenami primer cadena'

# In[27]:

cadena_multili.find('es')


# Out[27]:

#     5

# In[29]:

get_ipython().magic(u'pinfo mi_cadena.encode')


# In[30]:

print "esta es una forma de escribir: " + mi_cadena


# Out[30]:

#     esta es una forma de escribir: mi primer cadena
# 

# In[31]:

print "esta es una forma de escribir: ", mi_cadena


# Out[31]:

#     esta es una forma de escribir:  mi primer cadena
# 

# In[33]:

print "esta es otra forma de escribir: %d" % (98)


# Out[33]:

#     esta es otra forma de escribir: 98
# 

##### Listas

# In[35]:

mi_primer_lista = [1, 2, 2, 2, 3, 4, 5, 'humano', 'perro', 3.9]
vacia = []


# In[36]:

mi_primer_lista.append('gato')
print mi_primer_lista


# Out[36]:

#     [1, 2, 2, 2, 3, 4, 5, 'humano', 'perro', 3.9, 'gato']
# 

# In[37]:

mi_primer_lista.count(2)


# Out[37]:

#     3

# In[38]:

len(mi_primer_lista)


# Out[38]:

#     11

# In[40]:

mi_primer_lista[10]


# Out[40]:

#     'gato'

# In[41]:

mi_primer_lista.reverse()
print mi_primer_lista


# Out[41]:

#     ['gato', 3.9, 'perro', 'humano', 5, 4, 3, 2, 2, 2, 1]
# 

##### tuplas

# In[42]:

mi_tupla = (1, 3, 4, 5, 'hola')
mi_tupla.


# Out[42]:

#     (1, 3, 4, 5, 'hola')

# In[43]:

mi_tupla.index(4)


# Out[43]:

#     2

# In[44]:

1 in mi_tupla


# Out[44]:

#     True

# #### Diccionarios

# In[48]:

mi_diccionario = {'ind_0':{'dni':35171569, 'sexo':'F'}, 'ind_1': 30883685}


# In[53]:

mi_diccionario['ind_1']['dni']


# Out[53]:


    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    <ipython-input-53-a6fdf3d141c5> in <module>()
    ----> 1 mi_diccionario['ind_1']['dni']
    

    TypeError: 'int' object has no attribute '__getitem__'


# In[54]:

mi_diccionario.items()


# Out[54]:

#     [('ind_1', 30883685), ('ind_0', {'dni': 35171569, 'sexo': 'F'})]

# In[58]:

mi_diccionario['ind_4'] = [12345, 6789]


# In[59]:

mi_diccionario


# Out[59]:

#     {'ind_0': {'dni': 35171569, 'sexo': 'F'},
#      'ind_1': 30883685,
#      'ind_2': 123456789,
#      'ind_4': [12345, 6789]}

# In[60]:

mi_diccionario.values()


# Out[60]:

#     [[12345, 6789], 123456789, 30883685, {'dni': 35171569, 'sexo': 'F'}]

# In[75]:

lista = mi_diccionario.keys()
print lista
lista.reverse()
print lista


# Out[75]:

#     ['ind_4', 'ind_2', 'ind_1', 'ind_0']
#     ['ind_0', 'ind_1', 'ind_2', 'ind_4']
# 

##### Asignaciones

# In[76]:

x = 9.0
y = 2.0 + x
z = x + y
x, y, z


# Out[76]:

#     (9.0, 11.0, 20.0)

# In[78]:

x = 10
x = x + 5
x


# Out[78]:

#     15

# In[92]:

x += 2
#x -= 1
x


# Out[92]:

#     43

# In[93]:

x, y, z = 1, 2, 3
x, y, z


# Out[93]:

#     (1, 2, 3)

# In[94]:

z, x, y = x, y, z
x, y, z


# Out[94]:

#     (2, 3, 1)

# In[95]:

saludos = 'hola' + ', ' + 'como estas?'
saludos


# Out[95]:

#     'hola, como estas?'

###### Operadores de comparación

# In[98]:

type(saludos) == type('HOLA, COMO ESTAS?')


# Out[98]:

#     True

# In[97]:

saludos == 'hola, como estas?'


# Out[97]:

#     True

# In[100]:

z != 1


# Out[100]:

#     False

# In[102]:

x > y
x <= y


# Out[102]:

#     True

#### funciones Built-in de Python

# In[103]:

abs(-45)


# Out[103]:

#     45

# In[104]:

round(3.14159, 3)


# Out[104]:

#     3.142

# In[105]:

int(9.34)


# Out[105]:

#     9

# In[106]:

float(9)


# Out[106]:

#     9.0

# In[107]:

sum([1, 2, 3, 4, 5])


# Out[107]:

#     15

# In[108]:

min([1, 2, 3, 4, 5])


# Out[108]:

#     1

# In[109]:

len([1, 2, 3, 4, 5])


# Out[109]:

#     5

# In[110]:

from IPython.display import IFrame
IFrame('http://docs.python.org/library/functions.html', width=1000, height=350)


# Out[110]:

#     <IPython.lib.display.IFrame at 0x3f79dd0>

#### Escribiendo nuestras funciones

# In[112]:

def mi_funcion_saluda_a(nombre):
    """Esta funcion se encarga de saludar"""
    print "hola %s" %(nombre)



# In[114]:

get_ipython().magic(u'pinfo mi_funcion_saluda_a')


# In[115]:

mi_funcion_saluda_a('celia')


# Out[115]:

#     hola celia
# 

# In[116]:

def mi_suma(primer, segundo, tercer):
    return primer + segundo + tercer


# In[122]:

mi_suma(1, 2, 3)

def mi_mult():
    pass

mi_mult()


##### Condicionales

# In[124]:

columnas = ['Nombre', 'Apellido', 'Edad', 'Trabajo']


# In[128]:

if columnas != []:
    print 'esta lista no esta vacia'


# Out[128]:

#     esta lista no esta vacia
# 

# In[134]:

if columnas[-2] == 'Edad':
    print 'el último elemento de esta lista es Trabajo'


# Out[134]:

#     el último elemento de esta lista es Trabajo
# 

# In[139]:

columnas[:3]


# Out[139]:

#     ['Nombre', 'Apellido', 'Edad']

# In[140]:

x, y = 15, 3
if x < y:
    print 'x es menor que y'
else:
    print 'x es mayor que y'


# Out[140]:

#     x es mayor que y
# 

# In[141]:

x, y, z = 1, 2, 3
if x < y and x < z:
    print 'x es menor que z e y'

if z < x:
    print 'z es menor que x'
elif y < z:
    print 'y es menor que z'


# Out[141]:

#     x es menor que z e y
#     y es menor que z
# 

##### Loops

# In[142]:

i = 0
while i < 10:
    print 'ahora i vale %d' % (i)
    i += 1


# Out[142]:

#     ahora i vale 0
#     ahora i vale 1
#     ahora i vale 2
#     ahora i vale 3
#     ahora i vale 4
#     ahora i vale 5
#     ahora i vale 6
#     ahora i vale 7
#     ahora i vale 8
#     ahora i vale 9
# 

# In[146]:

i = 0
while i < 10:
    print 'ahora i vale %d' % (i)
    i += 1
    if i == 5:
        print 'el valor %d es el que yo buscaba!' % (i)
        break


# Out[146]:

#     ahora i vale 0
#     ahora i vale 1
#     ahora i vale 2
#     ahora i vale 3
#     ahora i vale 4
#     el valor 5 es el que yo buscaba!
# 

# In[147]:

for i in range(10):
    print 'ahora i vale %d' % (i)
    


# Out[147]:

#     ahora i vale 0
#     ahora i vale 1
#     ahora i vale 2
#     ahora i vale 3
#     ahora i vale 4
#     ahora i vale 5
#     ahora i vale 6
#     ahora i vale 7
#     ahora i vale 8
#     ahora i vale 9
# 

# In[150]:

mi_lista = range(10)
min(mi_lista)


# Out[150]:

#     0

# In[151]:

for c in columnas:
    print c


# Out[151]:

#     Nombre
#     Apellido
#     Edad
#     Trabajo
# 

# In[152]:

for c in range(len(columnas)):
    print columnas[c]


# Out[152]:

#     Nombre
#     Apellido
#     Edad
#     Trabajo
# 

# In[153]:

range(1, 10)


# Out[153]:

#     [1, 2, 3, 4, 5, 6, 7, 8, 9]

# In[154]:

range(2, 10)


# Out[154]:

#     [2, 3, 4, 5, 6, 7, 8, 9]

# In[156]:

range(0, 10, 2)
get_ipython().magic(u'pinfo range')

