import dill
import base64

class Queue():
    def __init__(self):
        self.data = []
    def add(self, item):
        self.data.append(item)
    def pop(self):
        return self.data.pop(0)

firstQueue = Queue()
firstQueue.add(1232312323)
firstQueue.add('adbcasdsd')
firstQueue.add(False)
nestedQueue = Queue()
nestedQueue.add('hello world')
firstQueue.add(nestedQueue)



data = dill.dumps(firstQueue)
data = base64.b64encode(data)
print(data)