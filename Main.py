

#Zadanie 5 (4pkt):
#Napisz funkcję, która sprawdzi poprawność kodu javy, używając obiektu z poprzedniego zadania
# i uwzględniając tylko nawiasy w kodzie.
#funkcja ma zwrocic True albo False w zależności czy kod jest poprawny czy nie.

def validation(kod_o):
    #zamiast pass napisz swój kod
    pass
wynik5 = validation(kod_o=obiekt)
print(wynik5)

#Zadanie 1 (4pkt):
#Utwórz klasę iteratora dla listy. Użyj go do wstawienia elementów listy lista1 do strina.
# elementy mają znajdować się w stringu jednym wierszu niczym nierozdzielone:

class Iterator:
  def __init__(self, list):
    self.list = list
    self.index = 0
  def __iter__(self):
    return self
  def __next__(self):
    if self.index >= len(self.list):
      raise StopIteration
    else:
      e = self.list[self.index]
      self.index +=1
      return e

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
iter_lista1 = Iterator(lista1)
tmp = ""
for e in iter_lista1:
  tmp = tmp + str(e)
wynik1 = tmp

print(wynik1)

#Zadanie2: (4pkt)
#Napisz funkcję fizzbuzz(n), która używając listy składanej zwróci
#listę od 1 do n włącznie liczb lub wyrazów Fizz, Buzz, FizzBuzz, zgodnie ze standradową
#reguła gry w FizzBuzz:
#Jeśli liczba jest podzielna przez 3 i niepodzielna przez 5, zamiast liczby mamy "Fizz".
#Jeśli liczba jest podzielna przez 5 i niepodzielna przez 3, zamiast liczby mamy "Buzz".
#Jeśli liczba jest zarówno podzielna przez 3, jak i przez 5, zamiast liczby mamy "FizzBuzz".
def fizbuzz(n):
    fizz_list = [c if c%3 != 0 and c%5 != 0 else "Fizz" if c%3 == 0 and c%5 != 0 else "Buzz" if c%3 != 0 and c%5 == 0 else "FizzBuzz" for c in range(1, n)]
    return fizz_list
wynik2 = fizbuzz(16)
print(wynik2)

#Zadanie 3 (4pkt):
#Napisz generator zwracający n wyrazów ciągu Lucasa
#do wyniku zapisz 6 element tego ciągu.

def lucas(n):
  last = 0
  before_last = 0
  for e in range (n):
    if e == 0:
      yield 2
      before_last = last
      last = 2
    elif e == 1:
      yield 1
      before_last = last
      last = 1
    elif e > 1:
      yield last + before_last
      tmp = last + before_last
      before_last = last
      last = tmp


gen_lucas = lucas(10)
for e in range(5):
  next(gen_lucas)
wynik3 = next(gen_lucas)
print(wynik3)

#Zadanie4 (4pkt):
#Uzyj klasy napisanej na ostatnich zajęciach - wersji z iteratorem (wklej tutaj klasę)
#Do przechowywania znaków kodu javy z pliku Main.java.
class ListIterator:
  def __init__(self, lista):
    self.lista = lista
    self.index = 0
  def __iter__(self):
    return self
  def __next__(self):
    if self.index >= len(self.lista):
      raise StopIteration
    else:
      e = self.lista[self.index]
      self.index += 1
      return e

obiekt = " tutaj utworz obiekt tej klasy."
wynik4="wstaw w wynik4"
#następnie wstaw do niej znaki z kodu javy, które wczytasz z pliku Main.java
#ODKOMENTUJ poniższą linijkę, gdy utworzysz obiekt i dodasz do niego znaki:
'''
!odkomentuj wynik4!:
'''
#wynik4 = obiekt.size()
print(wynik4)