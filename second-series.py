user_input = int(input("Enter the limit: "))
user_position = int(input("Enter the position: "))
final_list = []

class secondSeries:
  def prime(self, limit):
    self.prime_list = []
    self.count = 0
    for self.num in range(1, limit ** 2):
      if self.num > 1:
        for i in range(2,self.num):
          if (self.num % i) == 0:
            break
        else:
          self.count += 1
          self.prime_list.append(self.num)
        if self.count == limit:
          return self.prime_list

  def fibonacci(self, limit):
    self.n1 = 0
    self.n2 = 1
    self.fibonacci_list = []
    for i in range(0, limit):
      self.n3 = self.n1 + self.n2
      self.n1 = self.n2
      self.n2 = self.n3
      self.fibonacci_list.append(self.n1)
    return self.fibonacci_list

  def position(self, pos):
    return final_list[pos-1]

series = secondSeries()
for i, j in zip(series.fibonacci(user_input), series.prime(user_input)):
  final_list.append(i)
  final_list.append(j)

print(final_list)
print(series.position(user_position))
