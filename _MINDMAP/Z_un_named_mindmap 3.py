
'''
mindmap outputs html but not svg yet

'''

class Node:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __repr__(self):
        return f"Node({self.name}, {self.coordinates})"


class MindMap:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def connect_nodes(self, node1, node2):
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)

    def hide_names_at_zoom_level(self, zoom_level, name):
        for node in self.nodes:
            if node.name == name:
                node.hidden_at_zoom_level = zoom_level

    def display_cluster_relations(self, cluster_center, cluster_nodes):
        # TODO: Implement this method
        pass

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))

    def to_html(self):
        map_html = """
        <div id="mindmap">
            <svg width="500" height="500">
                <g>
    """

        for node in self.nodes:
            map_html += f"""
                    <circle cx="{node.coordinates[0]}" cy="{node.coordinates[1]}" r="10" fill="red" />
                    <text x="{node.coordinates[0]}" y="{node.coordinates[1] + 10}" font-size="12">{node.name}</text>
                """

        for node1, node2 in self.connections:
            map_html += f"""
                    <path d="M {node1.coordinates[0]} {node1.coordinates[1]} L {node2.coordinates[0]} {node2.coordinates[1]}" stroke="black" />
                """

        map_html += """
            </g>
        </svg>
    </div>
    """

        return map_html

    def __repr__(self):
        mindmap_string = ""

        for node in self.nodes:
            mindmap_string += f"{node}\n"

        return mindmap_string


# Example usage:

mindmap = MindMap()

# Create nodes
node1 = Node("Node 1", (1, 1))
node2 = Node("Node 2", (2, 2))
node3 = Node("Node 3", (3, 3))

# Add nodes to the mindmap
mindmap.add_node(node1)
mindmap.add_node(node2)
mindmap.add_node(node3)

# Connect the nodes
mindmap.connect_nodes(node1, node2)
mindmap.connect_nodes(node2, node3)

# Hide certain names at certain levels
mindmap.hide_names_at_zoom_level(zoom_level=12, name="Node 3")

# Display cluster relations
mindmap.display_cluster_relations((1.5, 1.5), ["Node 1", "Node 2"])

# Save the mindmap
mindmap.save("mindmap.html")
