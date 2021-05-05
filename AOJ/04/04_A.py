from decimal import Decimal,ROUND_HALF_UP
a,b=map(int,input().split())
d=a//b
r=a%b
f=a/b
print(d,r,Decimal(str(f)).quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP))