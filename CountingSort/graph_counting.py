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
  
x = [0.009288738001487218, 0.011973318993113935, 0.01558747299714014, 0.018950074998429045, 0.021698486001696438]
y = list(map(lambda z: z**2, x))
  
desenhaGrafico(x,y)
