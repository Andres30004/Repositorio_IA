#Perceptron multicapa
import numpy as np
#Tasa de aprendizaje
delta = 0.4
#BIAS
#W0=-4
X0=1 
#Error cuadratico medio
ECM= 10
epocas=50
#W = np.array([1,0.9])
it= 0
Yobt = np.array([-1,-1,1,1])

#Entrada
X = np.array([[-1,-1],[-1,1],[1,-1],[1,1]])

Yd = np.array([0,1,1,0])

#Inicializar la semilla para crear valores random
np.random.seed(40)
neuronas_entrada= X.shape[1] #1 porque queremos la columna es decir las entradas
neuronas_salida= 1

W_entrada= -np.random.rand(neuronas_entrada,neuronas_entrada) #fila,columa
W0_entrada= -1*np.random.rand(1,neuronas_entrada)#1 porque solo pedimos una fila, con el numero de entradas

W_salida=-np.random.rand(neuronas_salida,neuronas_entrada)#fila,columna
W0_salida=-1*np.random.rand(1,neuronas_salida)

def escalon(z):
 return np.where(z >=0,1,0)

def bipolar(z):
  return np.where(z >=0,1,-1)

def sigmoide(z):
  return 1/(1+(np.exp(-z)))


while(ECM >= 0.2 and it<=epocas):
    for j in range (0, X.shape[0]): #evalua casos
        z_entrada = np.dot(W_entrada.T,X[j,:]) + W0_entrada*X0 #primera capa
        y_entrada = sigmoide(z_entrada) #primera capa

        z_salida =  np.dot(W_salida,y_entrada.T) + W0_salida * X0
        Yobt[j] = sigmoide(z_salida)

        if (Yobt[j] != Yd[j]):
          W_entrada = W_entrada + delta*(Yd[j]-Yobt[j])*X[j,:]
          W0_entrada = W0_entrada + delta*(Yd[j]-Yobt[j])
          W_salida = W_salida + delta*(Yd[j]-Yobt[j])*y_entrada
          W0_salida = W0_salida + delta*(Yd[j]-Yobt[j])

    ECM = (1/2)*np.sum((Yd-Yobt)**2)
    epoca = epoca +1
    print("Epoca: ", epoca)
    print("Y obt de la epoca: ", Yobt)

print("Y obt final: ", Yobt)