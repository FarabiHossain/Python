#stack and queue

#stack
books= []
books.append("learn c")
books.append("learn c++")
books.append("learn java")
books.append("Html")
print(books)

books.pop()
print(books)

books.pop()
print(books)

books.pop()
print(books)

books.pop()
print(books)

#queue
from collections import deque
bank =deque( ["x","y","a"])
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)

