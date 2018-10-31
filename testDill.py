import dill
import base64

class Queue():
    def __init__(self):
        self.data = []
    def add(self, item):
        self.data.append(item)
    def pop(self):
        return self.data.pop(0)

data = dill.dumps(Queue)
data = base64.b64encode(data)
print(data)