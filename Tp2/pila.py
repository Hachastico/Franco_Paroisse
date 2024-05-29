class Pila():
    def __init__(self):
        self.items = []

    def __eq__(self, stack_aux):
        if isinstance(stack_aux, Pila):
            return self.items == stack_aux.items
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() > 0:
            dato = self.items.pop()
            return dato

    def on_top(self):
        if self.size() > 0:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def obtain_elements(self):
        return self.items[:]

