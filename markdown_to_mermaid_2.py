import re

def markdown_to_mermaid(markdown_text):
  """Converts Markdown to Mermaid code.

  Args:
    markdown_text: A string containing Markdown text.

  Returns:
    A string containing Mermaid code.
  """

  # Split the Markdown text into lines.
  current_heading_level = 0
  lines = markdown_text.splitlines()

  # Create a Mermaid code string.
  mermaid_code = "(\n"

  # Iterate over the lines of Markdown text.
  for line in lines:
    # Remove the leading whitespace.
    line = line.lstrip()

    # Ignore empty lines.
    if not line:
      continue

    # Get the heading level.
    heading_level = len(re.findall(r"^#", line))

    # If the heading level is greater than the current heading level, add a
    # new Mermaid code block for the heading.
    if heading_level > current_heading_level:
      mermaid_code += "  " * (heading_level - 1) + f"{line}(\n"
      current_heading_level = heading_level

    # If the heading level is less than the current heading level, close the
    # Mermaid code block for the current heading.
    elif heading_level < current_heading_level:
      mermaid_code += "  " * (current_heading_level - heading_level) + ")\n"
      current_heading_level = heading_level

    # Otherwise, the heading level is the same as the current heading level,
    # so just add the line to the Mermaid code string.
    else:
      mermaid_code += "  " * heading_level + line + "\n"

  # Close the remaining Mermaid code blocks.
  for i in range(current_heading_level):
    mermaid_code += "  " * i + ")\n"

  # Return the Mermaid code string.
  return mermaid_code

# Example usage:

markdown_text = """
# h1
## h2
### h3
## h2
### h3
#### h4
"""

mermaid_code = markdown_to_mermaid(markdown_text)

print(mermaid_code)
