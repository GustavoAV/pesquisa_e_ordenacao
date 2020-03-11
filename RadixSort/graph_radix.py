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
  
x = [0.028834104538, 0.0436561107635, 0.0612571239471, 0.0798768997192, 0.122599840164]
y = list(map(lambda z: z**2, x))
  
desenhaGrafico(x,y)
