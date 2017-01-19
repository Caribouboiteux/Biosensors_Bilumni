import matplotlib.pyplot as plt
import numpy
import numpy.random as random
import math
import sys

inte = []        #modif les listes
dist = []
capt = []

fichier = open('test.csv', 'r')
data = fichier.readlines()
for raw in data:
	raw = raw.strip().split(',')
	inte.append(int(raw[0]))             #modif en fonction des listes
	dist.append(int(raw[1]))


moyint = []
moydist = []
moycapt = []

for i in range(len(inte)):
	moyint.append((inte1[i] + inte2[i] + inte3[i]) / 3)         #modif en fonction du nombre de réplicats
	moydist.append((dist1[i] + dist2[i] + dist3[i]) / 3)
	moycapt.append((capt1[i] + capt2[i] + capt3[i]) / 3)


plt.subplot(211)
plt.plot(inte, dist1, 'o', 'green', inte, dist2, 'o', 'green', inte, dist3, 'o', 'green', inte, moydist, 'o' )
plt.title("Dist in function of intensity")
plt.xlabel("inte(lux)")
plt.ylabel("dist(micromètre)")

plt.subplot(212)
plt.plot(inte, capt1, 'o', 'red', inte, capt2, 'o', 'red', inte, capt3, 'o', 'red', inte, moycapt, 'o')
plt.title("captor results")
plt.xlabel("intesity(lux)")
plt.ylabel("digital unities")
plt.tight_layout()

plt.show()
