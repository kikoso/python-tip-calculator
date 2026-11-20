# Outlook: priority queue with heapq (smallest number first)
import heapq

tasks = []
heapq.heappush(tasks, (2, "Mails beantworten"))
heapq.heappush(tasks, (1, "Server neu starten"))
heapq.heappush(tasks, (3, "Kaffee holen"))
print(heapq.heappop(tasks))
print(heapq.heappop(tasks))
