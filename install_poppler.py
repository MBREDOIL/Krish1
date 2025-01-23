import subprocess
import platform

def install_poppler():
    system = platform.system()

    if system == "Windows":
        print("Please download and install Poppler manually from https://github.com/oschwartz10612/poppler-windows/releases/")
        print("After downloading, extract the ZIP file and add the 'bin' directory to your system's PATH environment variable.")
    elif system == "Linux":
        try:
            subprocess.run(["sudo", "apt-get", "install", "-y", "poppler-utils"], check=True)
            print("Poppler installed successfully on Linux.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing Poppler on Linux: {e}")
    elif system == "Darwin":  # macOS
        try:
            subprocess.run(["brew", "install", "poppler"], check=True)
            print("Poppler installed successfully on macOS.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing Poppler on macOS: {e}")
    else:
        print(f"Unsupported operating system: {system}")

if __name__ == "__main__":
    install_poppler()
