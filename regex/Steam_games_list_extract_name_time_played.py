def process_game_list(text_block, stop_section="TOTAL PLAYED", unwanted_sections=("LAST PLAYED", "ACHIEVEMENTS", "My Game Stats", "My Game Content", "UNINSTALL", "DOWNLOAD")):
  """Processes a text block containing game data to separate entries and remove unwanted sections.

  Args:
      text_block: A string containing the game data.
      stop_section: The string marking the end of game information (defaults to "TOTAL PLAYED").
      unwanted_sections: A tuple containing strings of sections to remove (defaults to common unwanted sections).

  Returns:
      A string with processed game entries in the desired format.
  """
  processed_data = ""
  current_game = ""
  collecting_info = True  # Flag to track if we're collecting game info

  for line in text_block.splitlines():  # Split text block into lines
    # Identify game name and separate entries
    if line != stop_section:
      if line.strip():  # Check for non-empty lines (excluding stop section)
        collecting_info = True
        current_game += line + "\n"  # Concatenate lines for each game
    else:
      # Stop collecting info when encountering the stop section
      collecting_info = False
      if current_game:
        processed_data += current_game.rstrip("\n") + "\n\n"  # Add game with double newline
        current_game = ""
  # Add the last game entry (if any)
  if current_game and collecting_info:
    processed_data += current_game.rstrip("\n") + "\n\n"

  # Remove unwanted sections within each game entry
  for unwanted_section in unwanted_sections:
    processed_data = processed_data.replace(unwanted_section + "\n", "")

  return processed_data.rstrip("\n")  # Remove trailing newline

# Your text block containing game data
text_block = """Warframe
TOTAL PLAYED
1,887.2 hours
LAST PLAYED
May 19
ACHIEVEMENTS
174/193
My Game Stats
My Game Content
UNINSTALL
Factorio
Factorio
TOTAL PLAYED
532.4 hours
LAST PLAYED
Jun 24
ACHIEVEMENTS
20/38
My Game Stats
My Game Content
UNINSTALL
# ... (other games)
"""

# Process the game data
processed_text = process_game_list(text_block)

# Print the processed data
print(processed_text)
