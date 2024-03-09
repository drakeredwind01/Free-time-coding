def read_browsers(filename):
    '''Reads a list of browsers from a text file.

    Args:
      filename: The path to the text file.

    Returns:
      A list of browser names.
    '''
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def generate_html(browsers):
    html_content = f'''
<!DOCTYPE html>
<html>
  <body>

  <h1>The datalist element</h1>

  <form action="/action_page.php" method="get">
    <label for="browser">Choose your browser from the list:</label>
    <input list="browsers" name="browser" id="browser">
    <datalist id="browsers">
'''
    for browser in browsers:
        html_content += f"      <option value=\"{browser}\">\n"

    html_content += '''
    </datalist>
    <input type="submit">
  </form>

  <p><strong>Note:</strong> The datalist tag is not supported in Safari 12.0 (or earlier).</p>

  </body>
</html>
'''
    return html_content


def main():
    filename = "browsers.txt"  # Replace with your actual filename
    browsers = read_browsers(filename)
    html_content = generate_html(browsers)
    with open("browser_datalist.html", "w") as f:
        f.write(html_content)

    print("HTML code written to browser_datalist.html")


if __name__ == "__main__":
    main()