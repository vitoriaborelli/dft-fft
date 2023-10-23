import numpy as np
"ALGORITMO DA DFT - TRANSFORMADA DISCRETA DE FOURIER"
def DFT_slow(x):
    # inicializa as variáveis com os dados do sinal de entrada
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    # calcula os cofatores
    M = np.exp(-2j * np.pi * k * n / N)
    # plota o vetor obrtido após o processamento do sinal
    return np.dot(M, x)
"----------------------------------------------------"
"ALGORITMO DA FFT - TRANSFORMADA RÁPIDA DE FOURIER"
def FFT(x):
    """Implementação recursiva do FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    
    if N % 2 > 0:
        raise ValueError("Deve ser multiplo de 2")
    elif N <= 32:  # critério para divisão do problema ou não
                   # Define quando deve ser solucionado de forma "bruta"
        return DFT_slow(x)
    else:
        # Divide o sinal de entrada em sub-vetores e calcula recursivamente
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        # Concatena os vetores calculados e gera o vetor final
        return np.concatenate([X_even + factor[:N // 2] * X_odd,
                               X_even + factor[N // 2:] * X_odd])
"----------------------------------------------------"
"ALGORITMO DA FFT VETORIZADA - TRANSFORMADA RÁPIDA DE FOURIER VETORIZADA"
def FFT_vectorized(x):
    """Uma versão vetorizada e não recursiva do FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if np.log2(N) % 1 > 0:
        raise ValueError("Deve ser multiplo de 2")

    #N_min é equivalente a condição de parada acima e deve ser um múltiplo de 2
    N_min = min(N, 32) 
    
    # Executa uma DFT de ordem O[N^2] sobre todos os problemas de tamanho N_min de uma vez
    n = np.arange(N_min)
    k = n[:, None]
    M = np.exp(-2j * np.pi * n * k / N_min)
    X = np.dot(M, x.reshape((N_min, -1)))

    # Gera o novo vetor com os cofatores calculados de forma recursiva
    while X.shape[0] < N:
        X_even = X[:, :X.shape[1] // 2]
        X_odd = X[:, X.shape[1] // 2:]
        factor = np.exp(-1j * np.pi * np.arange(X.shape[0])
                        / X.shape[0])[:, None]
        X = np.vstack([X_even + factor * X_odd,
                       X_even - factor * X_odd])

    return X.ravel()
"----------------------------------------------------"
"Comparação dos resultados para diferentes valores de N (número de elementos do vet):"

print('COMPARAÇÃO COM N = 1024:\n')
x = np.random.random(1024) #Gera um vetor de tamanho N com elementos aleatórios
%timeit DFT_slow(x) 
%timeit FFT(x)
%timeit FFT_vectorized(x)

print('\nCOMPARAÇÃO COM N = 2048:\n')
x = np.random.random(2048)
%timeit DFT_slow(x)
%timeit FFT(x)
%timeit FFT_vectorized(x)

print('\nCOMPARAÇÃO COM N = 4096:\n')
x = np.random.random(4096)
%timeit DFT_slow(x)
%timeit FFT(x)
%timeit FFT_vectorized(x)

"----------------------------------------------------"
"Exibição dos Gráficos de Comparação de Desempenho"

import matplotlib.pyplot as plt
import time

# inicializando os pontos e seus valores
eixo_x = [512, 1024, 2048, 4096, 8192, 16384]
eixo_y1 = [0,0,0,0,0,0]
eixo_y2 = [0,0,0,0,0,0]
eixo_y3 = [0,0,0,0,0,0]

# obtendo os tempos de execução de cada algoritmo e setando como eixo y
for i in range(6):

  # DFT
  start1 = time.time()
  DFT_slow(np.random.random(eixo_x[i]))
  end1 = time.time() 
  eixo_y1[i] = end1 - start1 

  # FFT
  start2 = time.time()
  FFT(np.random.random(eixo_x[i])) 
  end2 = time.time()
  eixo_y2[i] = end2 - start2 

  # FFT vetorizada
  start3 = time.time()
  FFT_vectorized(np.random.random(eixo_x[i])) 
  end3 = time.time()
  eixo_y3[i] = end3 - start3 

# exibição do gráfico DFT x FFT x FFT vetorizada
print('\nANÁLISE GRÁFICA GERAL\n')
plt.plot(eixo_x, eixo_y1)
plt.plot(eixo_x, eixo_y2)
plt.plot(eixo_x, eixo_y3)
plt.title('Comparação de Desempenhos')
plt.legend(['DFT','FFT', 'FFT vetorizada'])
plt.xlabel('Magnitude da Entrada')
plt.ylabel('Tempo de Execução')
plt.show()

# exibição do gráfico FFT x FFT vetorizada
print('\nANÁLISE GRÁFICA FFT X FFT VETORIZADA\n')
plt.plot(eixo_x, eixo_y2)
plt.plot(eixo_x, eixo_y3)
plt.title('Comparação de Desempenhos')
plt.legend(['FFT', 'FFT vetorizada'])
plt.xlabel('Magnitude da Entrada')
plt.ylabel('Tempo de Execução')
plt.show()
