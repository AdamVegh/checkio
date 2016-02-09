__author__ = 'Vegh Adam'


class Friends:
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        not_conn = connection not in self.connections
        if not_conn:
            self.connections += [connection]
        return not_conn

    def remove(self, connection):
        conn = connection in self.connections
        if conn:
            self.connections.remove(connection)
        return conn

    def names(self):
        set_friends = set()
        for connection in self.connections:
            set_friends |= connection
        return set_friends

    def connected(self, name):
        set_friends = set()
        for connection in self.connections:
            if name in connection:
                set_friends |= connection - {name}
        return set_friends
