class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index = 0  # a counter to insert into the list

    def append(self, item):
        if len(self.data) < self.capacity:  # this wont take effect until we hit our max capacity
            self.data.append(item)
        else:  # override our oldest index item and when we hit it's capacity, replace it with the newest item being inserted
            self.data[self.index] = item
            self.index = (self.index + 1) % self.capacity

    def get(self):
        return self.data
