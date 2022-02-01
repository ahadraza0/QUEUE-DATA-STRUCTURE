from collections import deque
q=deque()
q.append("ahadraza")
q.append("ahsanraza")
q.append("aliraza")
print("initial")
print(q)

#removing elements through collections method of queues:
print("elements dequeued from the queues")
print(q.popleft())
print(q.popleft())
print(q.popleft())
print("queues after removing elements")
print(q)