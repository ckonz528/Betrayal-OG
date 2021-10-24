class Manager:
    def __init__(self):
        self.systems = {}
        self.order = []
        self.num_entities = 0

    def register_sys(self, cls, comp_type):
        self.systems[comp_type] = cls(comp_type)
        self.order.append(comp_type)

    def add_entity(self, **components):
        new_ent = self.num_entities
        self.num_entities += 1

        for comp_type in components:
            self.systems[comp_type].add_component(new_ent, comp_type)

        return new_ent

    def get_sys(self, comp_type):
        return self.systems[comp_type]

    def broadcast(self, msg):
        for sys in self.systems.values():
            if msg.msg_type in sys.message_types:
                sys.accept_msg(msg)

    def process_sys(self):
        for comp_type in self.order:
            self.systems[comp_type].process()

    def get_component(self, entity, comp_type):
        self.systems[comp_type].get_component(entity)

    def remove_entity(self, entity):
        for sys in self.systems.values():
            if sys.contains(entity):
                sys.remove_component(entity)

    def has_components(self, entity, *comp_types):
        for comp in comp_types:
            if not self.systems[comp].contains(entity):
                return False

        return True


class Message:
    def __init__(self, msg_type, data):
        self.msg_type = msg_type
        self.data = data
