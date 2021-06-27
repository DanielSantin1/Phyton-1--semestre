x=float(input("hora de início:"))
y=float(input("hora de fim:"))
mx=x*60
my=y*60

if(my>=mx):
    h=(my-mx)/60
else:
    h=(1440-mx)+my/60
print("duração foi:",h)