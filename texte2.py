hor=float(input("hora de início:"))
horf=float(input("hora de termino:"))

mx=hor*60
my=horf*60


if(my>=mx):
    k=(my-mx)/60
minc=float(input("min de início:"))
minf=float(input("min de termino:"))

mz=hor*60
mn=horf*60
if(mn>=mz):
    h=(mn-mz)/60
l=k+h
print("duração foi:",l)