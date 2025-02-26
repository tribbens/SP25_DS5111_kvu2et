import platform
import sys

print(sys.version[:4])
print(type(sys.version))

def test_os():
    assert platform.system() == "Linux", "wrong operating system, use a Linux system"

def test_python():
    assert sys.version[:4] in ["3.10", "3.11"], "wrong version of python, use 3.10 or 3.11"
