from heapq import heappush, heappop


class StackFringe:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        return self.stack.pop()

    def push(self, loc):
        if loc in self.stack:
            return
        else:
            return self.stack.append(loc)


class QueueFringe:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, loc):
        return self.queue.insert(0, loc)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()


class HeapFringe:
    def __init__(self):
        self.heap = []
        self.node_lookup = {}

    def add_node(self, node):
        self.node_lookup[node.loc] = node
        heappush(self.heap, node)

    def is_empty(self):
        return len(self.heap) == 0

    def get_min_node(self):
        while not self.is_empty():
            node = heappop(self.heap)
            if node.is_valid():
                del self.node_lookup[node.loc]
                return node
        return None

    def update_node(self, node):
        old_node = self.node_lookup[node.loc]
        old_node.set_invalid()
        self.add_node(node)
