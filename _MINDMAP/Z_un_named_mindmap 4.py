import webbrowser

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
        self.connections = []

    def add_node(self, node):
        self.nodes.append(node)

    def connect_nodes(self, node1, node2):
        self.connections.append((node1, node2))

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
            <svg width="1000000" height="1000000">
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
node1 = Node("Lee", (170.02,189.4))
node2 = Node("Robertson", (216.67,276.4))
node3 = Node("Bederson", (537.18,570.5))
node4 = Node("Nachmanson", (410.55,1105.5))
node5 = Node("Tóth", (325.2,394.21))
node6 = Node("Kyncl", (662.2,354.41))
node7 = Node("Pinchasi", (2101,372.82))
node8 = Node("Cerný", (578.6,378.07))
node9 = Node("Keszegh", (360.5,374.88))
node10 = Node("Pálvölgyi", (177.7,354.65))

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

# Get the SVG code for the mindmap
svg_code = mindmap.to_html()

# Insert the SVG code into the HTML file
with open("mindmap.html", "w") as f:
    f.write(svg_code)

# Open the HTML file in a web browser
webbrowser.open("mindmap.html")
