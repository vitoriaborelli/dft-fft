# Algoritmos DFT e FFT
Implementação e análise comparatória entre os algoritmos da DFT, FFT e FFT vetorizada.

O trabalho trata-se da implementação e comparação entre os algoritmos DFT (Discret Fourier Transformation) e FFT (Fast Fourier Transformation). Tais códigos são baseados, assim como indicado em seus nomes, na ferramenta "Transformação de Fourier", utilizada para estudar variados tipos de sinais em função de seus componentes de frequência, possibilitando sua análise e processamento. Ambos os métodos têm seus funcionamentos explicados mais detalhadamente, explicitando também suas diferenças.

## DFT
A DFT, também chamada de Transformada Discreta de Fourier, se trata de um método matemático para a análise de sinais digitais e analógicos. Muito usado no ramo das telecomunicações e implementada através de conhecimentos computacionais, a transformada, por meio da chamada série de Fourier, que traduz um sinal de onda em funções de seno e cosseno, é responsável por sintetizar o sinal que é captado como "amplitude X tempo" na forma de "frequência X amplitude".

## FFT
A FFT, também chamada de Trasformada Rápida de Fourir se trata, por sua vez, como o próprio nome denota, de um aprimoramento no desempenho computacional do algoritmo da DFT. Isso se dá pois, enquanto o algoritmo da transformada discreta usa basicamente da "força bruta", a FFT faz uso da estratégia de dividir para conquistar e consequemente, recursão, a fim de diminuir o custo computacional do algoritmo.

## FFT Vetorizada
Por fim, é apresentado o algoritmo FFT de forma vetorizada, na qual há, novamente, melhoria na eficiência de tempo. Isso se dá pois, na implementação anterior, eram executadas repetidas multiplicações entre matrizes e vetores; no entanto, deste modo tais vetores são unidos formando uma matriz, reduzindo tais operações a uma única multiplicação entre matrizes.

De forma sucinta, o aspecto essencial que diferencia tal algoritmo do anterior é a forma de tratamento das operações, rearranjando-as de forma a tratá-las como vetores. Tal mudança pode ser útil principalmente tratando-se das simetrias mencionadas anteriormente, possibilitando ainda que alguns vetores possam ser reduzidos ao meio, por exemplo.
