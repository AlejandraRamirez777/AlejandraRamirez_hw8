import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sc

#FUncion que retorna la distribucion normal de acuerdo a su formula
#con promedio mean y desviacion estandar sigma

def normal_dist(x,mean,sigma):
    a = np.sqrt(1/float(2*np.pi*(sigma**2)))
    c = (x-mean)**2
    b = np.exp(-1*(c)/float(sigma**2))
    sol = a*b
    return sol

#Funcion que carga array de promedios
#y genera histograma a partir de los datos cargados

def get_fit(filename):
    #Carga los datos
    data = np.genfromtxt(filename, usecols = 0)
    #Retorna frecuencias y limites de hist
    freqs,bins = np.histogram(data, normed = True)
    data
    
    #Optimizar curva
    #frecuencias
    y = freqs
    #bins
    x = 0.5*(bins[:-1]+bins[1:]) 
    #funcion de optimizacion
    popt, pcov = sc.curve_fit(normal_dist,x,y)
    mean = popt[0]
    sigma = popt[1]
    xx = np.linspace(np.min(data),np.max(data),100)
    yy = normal_dist(xx,mean,sigma)

    plt.plot(xx,yy, label = "ajuste normal")
    plt.hist(data)
    plt.savefig(filename+str(".png"))
    plt.clf()

K = ["sample_1_10.txt","sample_1_100.txt","sample_1_1000.txt","sample_2_10.txt","sample_2_100.txt","sample_2_1000.txt"]
for i in K:
    get_fit(K)
    
    


