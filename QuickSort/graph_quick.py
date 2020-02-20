import matplotlib as mpl
import matplotlib.pyplot as plt

def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()
  
x = [53.3690019, 107.13113729999999, 169.6448829, 235.26773379999997, 299.07608089999997]
y = list(map(lambda z: z**2, x))
  
desenhaGrafico(x,y)
