from collections import deque
queue = deque(["sambhaji", "sadhana"])

print(queue)

queue.append("satyam")
print(queue)

queue.append("aaradhya")
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)