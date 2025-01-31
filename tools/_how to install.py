
import https://www.tensorflow.org/install/source_windows


for (install latest):
    conda install cudatoolkit=11.2 cudnn=8.1 -c=conda-forge
    pip install tensorflow-gpu==2.9
for (install to use media):
    pip install opencv-python
    blank


def install_other_version(package,version):
    print(f'pip uninstall {package} --y')
    print(f'pip cache purge')
    print(f'pip install {package}=={version}')

import subprocess

def install_other_version(package, version):
    """
    Installs a specific version of a Python package.

    Args:
        package (str): The name of the package to install.
        version (str): The specific version of the package to install.
    """

    try:
        # Uninstall the existing package
        subprocess.run(["pip", "uninstall", package, "-y"], check=True)

        # Clear the pip cache
        subprocess.run(["pip", "cache", "purge"], check=True)

        # Install the specified version
        subprocess.run(["pip", "install", f"{package}=={version}"], check=True)

        print(f"Successfully installed {package} version {version}")

    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")

# Example usage
install_other_version("torch", "1.13.1")







