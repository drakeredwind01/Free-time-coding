'''

trying to use pygraphviz

'''
import pygraphviz as pgv
import svgwrite

def graph_to_svg(graph_file, svg_file):
  """Converts a graph file to SVG.

  Args:
    graph_file: The path to the graph file.
    svg_file: The path to the output SVG file.
  """

  graph = pgv.AGraph(graph_file)

  # Create an SVG document
  svg = svgwrite.Drawing(svg_file)

  # Add the graph nodes and edges to the SVG document
  for node in graph.nodes():
    svg.add(svgwrite.circle(node.attr['pos'], r=10, fill='red'))
    svg.add(svgwrite.text(node.attr['label'], node.attr['pos'], fill='black'))

  for edge in graph.edges():
    svg.add(svgwrite.path(d=f'M {edge.attr["src"]["pos"]} L {edge.attr["dst"]["pos"]}', stroke='black'))

  # Save the SVG document
  svg.save()

if __name__ == '__main__':
  graph_file = 'django_relations.dot'
  svg_file = 'django_relations.svg'

  graph_to_svg(graph_file, svg_file)
