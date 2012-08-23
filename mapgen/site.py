from pyglet import gl, graphics

class Site(object):
    def __init__(self, point, edges):
        self.point = point
        self.edge = Site._create_chain(edges)
        self.gl_points = reduce(lambda x, y: x + y, self.edge, tuple())

    def draw(self):
        gl.glColor3f(1.0, 1.0, 1.0)
        graphics.draw(len(self.gl_points) // 2, gl.GL_POLYGON, ('v2i', self.gl_points))

    @staticmethod
    def _create_chain(edges):
        chain = list(edges[0])
        del edges[0]

        groups = Site._group_edges(edges)

        current_link = chain[0]
        while current_link:
            current_link = Site._get_next_link(current_link, groups)
            if current_link:
                chain.insert(0, current_link)

        current_link = chain[-1]
        while current_link:
            current_link = Site._get_next_link(current_link, groups)
            if current_link:
                chain.append(current_link)

        if len(groups) > 0:
            raise Exception('Broken chain detected (%s)!' % chain, groups)

        return chain

    @staticmethod
    def _get_next_link(link, groups):
        if not link in groups:
            return
        edges = groups[link]
        if len(edges) < 2:
            del groups[link]
        current_edge = edges.pop()
        link = [x for x in current_edge if x != link][0]
        if link in groups:
            edges = groups[link]
            if current_edge in edges:
                edges.remove(current_edge)
            if len(edges) < 1:
                del groups[link]
        return link

    @staticmethod
    def _group_edges(edges):
        groups = {}
        for edge in edges:
            for vertex in edge:
                if not vertex in groups:
                    groups[vertex] = []
                if not edge in groups[vertex]:
                    groups[vertex].append(edge)
        return groups
