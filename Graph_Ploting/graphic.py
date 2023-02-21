import matplotlib.pyplot as plt

x = ['segunda', 'terça', 'quarta', 'quinta', 'sexta']
y = [0.54, 1.16, 1.48,0.41, 1.15]

plt.bar(x, y)
plt.title("Daily Active Code Time")
plt.xlabel("Dias")
plt.ylabel("Horas/minutos ativos)") 

plt.show()