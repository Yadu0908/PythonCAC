#here we can chnage our numbers into the digital number by using simple python methods


number = 128;
print(bin(number));
print(hex(number));
print(oct(number));

# Or we can also chnage them into by doing below method.

print(int('41', 8))


import random

print(random.randint(2,9));

#For choice we can also use the built-in function of random.

ch= ['Tea', 'Black coffee', 'Milk coffee', 'Red tea'];
random.choice(ch);      #It will give the choice from above list.

random.shuffle(ch);



print((0.1) + (0.1) + (0.1) - (0.3));

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))


set1= {1,2,3}

print(set1 & {2,3})     #For intersection.
print(set1 | {2,3})     #For union.
print(set1 - {2,3})     #For difference.

