class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None

  def isEmpty(self):
    return self.head is None

  def enqueue(self, data):
    new_node = Node(data)
    if self.isEmpty():
      self.head = self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

  def getNth(self, pos):
    if pos < 0 or pos >= self.size():
      return None

    current = self.head
    for i in range(pos):
      current = current.next
    return current.data

  def size(self):
    count = 0
    current = self.head
    while current:
      count += 1
      current = current.next
    return count

my_queue = Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
my_queue.enqueue("D")

third_element = my_queue.getNth(int(input("Ingresa la posicion que quieras obetener emepzando del 0: ")))

print(third_element) 