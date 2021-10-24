class System:
    def __init__(self, component_type):
        self._component_type = component_type
        self._components = {}
        self._message_types = []

    def add_component(self, entity, component):
        self._components[entity] = component

    def remove_component(self, entity):
        del self._components[entity]

    def get_component(self, entity):
        return self._components[entity]

    def contains(self, entity):
        return entity in self._components

    def accept_msg(self, msg):
        ...

    def process(self):
        ...
