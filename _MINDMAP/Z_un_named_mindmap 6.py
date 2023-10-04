import re
import svgwrite

def graph_to_svg(graph_file, svg_file):
  """Converts a graph file to SVG.

  Args:
    graph_file: The path to the graph file.
    svg_file: The path to the output SVG file.
  """

  # Read the graph file
  with open(graph_file, 'r') as f:
    graph_data = f.read()

  # Parse the graph data into a Python dictionary
  graph = {}
  for line in graph_data.splitlines():
    if line.startswith('node'):
      node_name = re.search(r'node \[label="([^"]*)"\]', line).group(1)
      node_pos = re.search(r'pos="([^"]*)"', line).group(1)
      graph[node_name] = {
        'pos': node_pos
      }
    elif line.startswith('edge'):
      src_node = re.search(r'src="([^"]*)"', line).group(1)
      dst_node = re.search(r'dst="([^"]*)"', line).group(1)
      graph[src_node]['edges'] = graph[src_node].get('edges', []) + [dst_node]

  # Create an SVG document
  svg = svgwrite.Drawing(svg_file)

  # Add the graph nodes and edges to the SVG document
  for node_name, node_data in graph.items():
    svg.add(svgwrite.circle(node_data['pos'], r=10, fill='red'))
    svg.add(svgwrite.text(node_name, node_data['pos'], fill='black'))

    for edge in node_data.get('edges', []):
      svg.add(svgwrite.path(d=f'M {node_data["pos"]} L {graph[edge]["pos"]}', stroke='black'))

  # Save the SVG document
  svg.save()

if __name__ == '__main__':
  graph_file = 'z_test_mindmap.rwg'
  svg_file = 'django_relations.svg'

  graph_to_svg(graph_file, svg_file)
