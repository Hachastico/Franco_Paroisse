class Cola():

    def __init__(self):
        self.__elementos = []

    def arrive(self, value):
        self.__elementos.append(value)

    def atention(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

    def size(self):
        return len(self.__elementos)

    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux
    
    #Metodo para que 'Cola()' sea iterable
    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index < self.size():
            result = self.__elementos[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration