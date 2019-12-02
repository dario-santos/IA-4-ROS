import Object

class Room:
    def __init__(self, objects : [Object]):
        self.objects = objects

    # Adicionar objeto
    def AddObject(self, name):
        info = name.split("_", 1)
        # Categoria, Nome
        obj = Object(info[0], info[1])

        self.objects.append(obj)


    # Remover objeto
    def RemoveObject(self, name):
        info = name.split("_", 1)
        obj = Object(info[0], info[1])

        self.objects.remove(obj)

    # buscar objeto pelo nome
    def GetObjectByName(self, name):
        for _, o in enumerate(self.objects):
            if o.getName() is name:
                return o
        return None

        

    # Buscar Objetos de uma categoria
    def GetObjectsByCategory(self, category):
        objects = []
        for _, o in enumerate(self.objects):
            if o.getCategory() is category:
                objects.append(o)

        return objects
