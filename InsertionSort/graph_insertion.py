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
  
x = [0.00016716899699531496, 0.0017462669929955155, 0.0051660750032169744, 0.011712150007952005]
y = list(map(lambda z: z**2, x))
  
desenhaGrafico(x,y)
