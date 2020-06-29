class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.current = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            # this takes the first index (which is the least used item in our list and replaces it with our new item)
            self.storage[self.current] = item
            self.current += 1

        #once we get to the end our of list it resets the index back to 0
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        return self.storage
