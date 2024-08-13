import random
from .models import PrototypeToken
def CreateToken():
  c =num = random.random()
  list1 = [1, 2, 3, 4, 5, 6]
  D = random.choice(list1)
  token = (D*c+D*c)
  PrototypeToken.objects.create(token = token )
  return token
  
