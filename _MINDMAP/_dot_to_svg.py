from pydot import graph_from_dot_file

# Replace 'Python Builtins MPP=20.dot' with the actual filename
dot_file_path = "Python Builtins MPP=20.dot"

try:
    graphs = graph_from_dot_file(dot_file_path)

    # Assuming you want the first graph (index 0)
    graph = graphs[0]  # Access the first graph from the list
    graph.write_svg("output.svg", prog="dot")  # Replace "output.svg" with desired output filename
    print("Successfully converted DOT file to SVG!")
except FileNotFoundError:
    print(f"Error: DOT file '{dot_file_path}' not found.")
except Exception as e:
    print(f"An error occurred during conversion: {e}")
