medida = float(input('Uma distância em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida/10
hm = medida/100
km = medida /1000

print('A media de {}m corresponde a \n{}km, \n{}hm, \n{}dam, \n{:.0f}dm, \n{:.0f}cm e \n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))



