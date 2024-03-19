import numpy as np
import matplotlib.pyplot as plt
delta = 0.7
it = 0
ECM= 3
epocas=2000
ecm_values = []

#W = np.array([1,0.9])
epoca = 0
#Yobt = np.array([-1.0,-1.0,1.0,1.0])
#Yobt= np.array([0.0,0.0,0.0,0.0])
#Entrada
X = np.array([[-1, 0, 0], [-1, 0, 1], [-1, 1, 0], [-1, 1, 1]])

Yd = np.array([[0], [1], [1], [0]])


#Inicializar la semilla para crear valores random
neuronas_entrada= 3 
#neuronas_capa_oculta= 3
neuronas_salida= 1

W_entrada= 2*np.random.rand(X.shape[1],neuronas_entrada) -1 #fila,columa
#W0_entrada= np.random.rand(1,neuronas_entrada)#1 porque solo pedimos una fila, con el numero de entradas

W_salida= 2*np.random.rand(neuronas_entrada+1,neuronas_salida)-1 #fila,columna
#W0_salida= np.random.rand(1,neuronas_salida)

W_new_entrada = np.zeros(W_entrada.shape)
W_old_entrada = np.zeros(W_entrada.shape)
W_new_salida = np.zeros(W_salida.shape)
W_old_salida = np.zeros(W_salida.shape)


def escalon(z):
 return np.where(z >=0.5,1,0)

def bipolar(z):
  return np.where(z >=0,1,-1)

def sigmoide(z):
  return 1.0/(1.0+(np.exp(-z)))

def deri_sig2(x):
  return np.exp(-x)/(1.0+np.exp(-x))**2

def deri_sig2(x):
  s = sigmoide(x)
  return s*(1-s)

def deri_sig(x):
  return x*(1-x)

def tanh(x):
  s = np.tanh(x)
  return s
def deriv_tanh(x):
  s = np.cosh(x)
  return  1/s**2

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

def deri_soft(x):
    s = softmax(x)
    return s * (1 - s)
alpha = 0.3

while(ECM >= 0.1 and epoca<=epocas):
    for j in range (0, X.shape[0]): #No es necesario el for
        z_entrada = np.dot(X,W_entrada) #primera capa
        y_entrada = np.insert(sigmoide(z_entrada),0,-1,axis=1) #primera capa
        #print(y_entrada)
        z_salida =  np.dot(y_entrada,W_salida)
        Yobt = sigmoide(z_salida)
        #print(Yobt[j])
#--------------------------Actualizacion de pesos---------------------
        
        aux = (Yd-Yobt)*deri_sig(Yobt) 
        aux3 = np.dot(aux,W_salida[1:, :].T)*deri_sig(y_entrada[:,1:]) #Parte desde la columna 1 y no la columna 0 [1:, :], [:, 1:] parte desde la fila 1 y no la fila 0 

        W_new_salida = W_salida + alpha * (W_salida-W_old_salida)+delta*np.dot(y_entrada,aux)
        W_old_salida = W_salida
        W_salida = W_new_salida

        W_new_entrada = W_entrada + alpha*(W_entrada - W_old_entrada)+ delta*np.dot(X.T,aux3)
        W_old_entrada = W_entrada
        W_entrada = W_new_entrada


    ECM = (1/2)*np.sum((Yd-Yobt)**2)
    ecm_values.append(ECM)  # Almacenar el valor actual de ECM
    epoca = epoca + 1
    print("Epoca: ", epoca)
    print("Y obt de la epoca: ", Yobt)

#Yobt = np.round(Yobt)

# Graficar el ECM a lo largo de las épocas
plt.plot(range(1, epoca+1), ecm_values, marker='o')
plt.xlabel('Época')
plt.ylabel('Error Cuadrático Medio (ECM)')
plt.title('Evolución del ECM durante el entrenamiento')
plt.grid(True)
plt.show()

print("Y obt final: ", np.round(Yobt))