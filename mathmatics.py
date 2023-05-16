'''m=float(input("도르래에 매달린 무게 :"))
r=float(input("반지름 :"))
a=float(input("접선가속도 :"))

f = m*r**2*((9.8/a)-1)

print(f)'''

e = float(input("실험값: "))
t = float(input("이론값: "))

p = abs((t-e)/t)*100

print(p)