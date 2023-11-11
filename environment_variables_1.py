import subprocess

def get_installed_software():
  """Returns a list of all of the software that is installed on the system."""

  output = subprocess.check_output(["wmic", "product", "get", "name"])
  installed_software = []
  for line in output.splitlines():
    installed_software.append(line.decode())
  return installed_software

def print_path_variables():
  """Prints out all of the variables that should be in %path%."""

  for installed_software in get_installed_software():
    print(installed_software)

if __name__ == "__main__":
  print_path_variables()
