class Site(object):
    def __init__(self, point, edges):
        self.point = point
        self.edge = self.build_edge(edges)

    def build_edge(self, edges):
        edge = list(edges[0])

        return edge
