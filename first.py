print("hello")

def test():
    tester = 1 + 2
    return tester

print(test())

def test_du_signe(valeur):
  if valeur < 0:
    print('négatif')
  elif valeur == 0:
    print('nul')
  else:
    print('positif')

test_du_signe(-2)