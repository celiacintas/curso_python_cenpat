
## Cómo instalar Python?

# - **GNU/LINUX**
# 
#     - ubuntu/debian
# \# apt-get install python-scipy python-matplotlib python-numpy python-qt4 python-pygments
#     - archlinux
# \# pacman -S python2-scipy ....
# 
# \# pip install pandas scikit-learn scikit-image statsmodels ipython
# 
# - **MAC OS**
# 
# 
#     - [SciPy SuperPack](http://fonnesbeck.github.io/ScipySuperpack/)
# 
# - **Distribuciones Cinetíficas de Python Multiplataforma** 
# 
# 
#     - [Python(X,Y)](http://code.google.com/p/pythonxy/)
#     - [Canopy](https://www.enthought.com/products/canopy/)
#     - [Anaconda](https://store.continuum.io/cshop/anaconda/)

# In[9]:

from IPython.display import IFrame
IFrame('http://continuum.io/downloads', width=700, height=350)


# Out[9]:

#     <IPython.lib.display.IFrame at 0x27d5310>

## Conociendo IPython

# ##Si queremos información de un módulo o función

# In[13]:

import numpy as np
from numpy import *
#np?
get_ipython().magic(u'pinfo reshape')


# ## Auto completado

# In[ ]:

np.array


# ## Historial

# In[14]:

12*2


# Out[14]:

#     24

# In[15]:

_ + 123


# Out[15]:

#     147

# In[17]:

# completar con valor actual _
_14


# Out[17]:

#     24

# ## Guardar y cargar sesiones en IPython

# In[18]:

import numpy as np
x = np.array([[1,2,3],[4,5,6]])
print np.transpose(x)


# Out[18]:

#     [[1 4]
#      [2 5]
#      [3 6]]
# 

# In[19]:

get_ipython().magic(u'save test_files/ex_1.py 18 # colocar nro de linea 1')


# Out[19]:

#     The following commands were written to file `test_files/ex_1.py`:
#     import numpy as np
#     x = np.array([[1,2,3],[4,5,6]])
#     print np.transpose(x)
#     import numpy as np
#     x = np.array([[1,2,3],[4,5,6]])
#     print np.transpose(x)
# 

# In[20]:

get_ipython().magic(u'load test_files/ex_1.py')


# In[21]:

import numpy as np
x = np.array([[1,2,3],[4,5,6]])
print np.transpose(x)


# Out[21]:

#     [[1 4]
#      [2 5]
#      [3 6]]
# 

# In[22]:

get_ipython().magic(u'run test_files/ex_1.py')


# Out[22]:

#     [[1 4]
#      [2 5]
#      [3 6]]
#     [[1 4]
#      [2 5]
#      [3 6]]
# 

# ## Qué hay en nuestras carpetas y archivos?

# ### Listando directorios

# In[23]:

ls 


# Out[23]:

#     Clase_0.01.ipynb  Class_0.ipynb  Class_1.ipynb  [0m[01;34mdata[0m/  [01;34mtest_files[0m/
# 

# In[24]:

ls data/


# Out[24]:

#     all_test.txt  test.csv
# 

# ### Dónde estamos trabajando ?

# In[25]:

pwd


# Out[25]:

#     u'/home/celia/Documents/CENPAT/curso_python/clases'

# ### Cambio de directorio de trabajo

# In[29]:

ls


# Out[29]:

#     all_test.txt  test.csv
# 

# ### Qué contienen nuestros archivos ? 

# In[32]:

more all_test.txt

