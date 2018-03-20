import numpy as np

#FUncion que genera y retorna N numeros aleatorios
#con distribucion discreta de probabilidad

def sample_1(N):
    #base de probabilidad
    num = np.array([-10,-5,3,9])
    #probabilidad
    pp = np.array([0.1,0.4,0.2,0.3])
    sol = np.random.choice(a = num,size = N,p=pp)
    return sol

#print sample_1(9)

#Funcion que genera y retorna N numeros aleatorios
#con distribucion exponencial

def sample_2(N):
    #Beta
    beta = 0.5
    sol = np.random.exponential(scale = beta, size=N)
    return sol

#print sample_2(7)

#Genera y retorna M promedios Sn a partir de funcion sampling_fun

def get_mean(sampling_fun,N,M):
    sol = np.zeros(M)
    #Calcula la media de cada muestra se que genera M veces (cada vez la muestra es diferente)
    for i in range(M):
        sol[i] = np.mean(sampling_fun(N))
    return sol

#Numero fijo
M = 10000
#Array N
N = [10,100,1000]

#Strings de nombres de archivos
s1 = "sample_1_"
s2 = "sample_2_"
en = ".txt"


#Genera cada elemento en N genera M promedios para sample_1 y sample_2
for i in N:
    #Crear los archivos para sample_1
    n1 = get_mean(sample_1,i,M)
    np.savetxt(s1 + str(i)+en,n1)
    #Crear los archivos para sample_2
    n2 = get_mean(sample_2,i,M)
    np.savetxt(s2 + str(i)+en,n2)
    
    	

