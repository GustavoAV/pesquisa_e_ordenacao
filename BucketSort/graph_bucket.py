import matplotlib as mpl
import matplotlib.pyplot as plt

def desenhaGrafico(x,y,xl = "Entradas", yl = "Saidas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()
  
x = [0.483468268008437, 1.317594745021779, 2.713141023996286, 5.790587177005364, 8.44085617599194]
y = list(map(lambda z: z**2, x))
  
desenhaGrafico(x,y)
