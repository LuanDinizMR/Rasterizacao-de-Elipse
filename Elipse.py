from math import sin, cos, radians
import matplotlib.pyplot as plt


def plot_pixel(x, y):
    # 's' = abreviação de square
    #marksize = tamanho do pixel
    plt.plot(x, y, marker='s', markersize=20, color='black')
    
def rasterizacao_elipse(a, b,h=0,k=0): 
#h e k = 0 caso não seja passado nenhum parametro

    for angulo in range (361):
        #radians transforma de graus para radianos
        plot_pixel(round(a*cos(radians(angulo))+h), round(b*sin(radians(angulo))+k))
        #plot_pixel(a*cos(radians(angulo))+h, b*sin(radians(angulo))+k)
    
    plt.title("Rasterização de Elipse")    
    plt.show()

print("Rasterização de Elipse")
while True:
    print("Digite o valor referente ao:")
    a = float(input("Comprimento do maior eixo: "))
    b = float(input("Comprimento do menor eixo: "))
    print("Digite as coordenadas do ponto central (x, y) da elipse: ")
    x = float(input("x: "))
    y = float(input("y: "))
    rasterizacao_elipse(a,b,x, y)
    
    resp = str(input("Deseja realizar outra operação? [S/N] ")).strip().upper().split()
    if resp[0] == 'N':
        break
    
    
