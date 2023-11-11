import re

def markdown_to_mermaid(markdown):
  """Converts Markdown to Mermaid.

  Args:
    markdown: A string containing Markdown text.

  Returns:
    A string containing Mermaid text.
  """

  # Remove any leading or trailing whitespace.
  markdown = markdown.strip()

  # Split the Markdown into lines.
  lines = markdown.splitlines()

  # Create a Mermaid graph.
  mermaid_graph = "( \n"

  # Iterate over the Markdown lines.
  for line in lines:
    # Ignore any lines that start with a hash (#).
    if line.startswith("#"):
      continue

    # Find the level of the heading (h1, h2, h3, etc.).
    heading_level = re.search(r"^(\#{1,6}) (.+)$", line).group(1)

    # Calculate the number of spaces to indent the heading.
    indent = (heading_level - 1) * 2

    # Add the heading to the Mermaid graph.
    mermaid_graph += f"  {' ' * indent}{heading_level}({line[len(heading_level) + 1:]}) \n"

  # Close the Mermaid graph.
  mermaid_graph += ")"

  return mermaid_graph

# Print the Mermaid output.
print(markdown_to_mermaid(markdown="""
# h1
## h2
### h3
## h2
### h3
#### h4
"""))
