import platform
import sys

print(sys.version[:4])
print(type(sys.version))

def test_os():
    assert platform.system() == "Linux", "wrong operating system, use a Linux system"

def test_python(): # head's up that this will have to change when you update the validations.yaml
    assert sys.version[:4] in ["3.10", "3.11", "3.12"], "wrong version of python, use 3.10, 3.11, or 3.12"
