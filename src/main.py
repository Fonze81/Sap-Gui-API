import sys
from sapguiapi import GuiComponent

def main():
    message: str = 'Hello'
    print(f'{message} World!')
    obj = GuiComponent()
    print(obj)
    print(type(obj))
    print(type(obj).__name__)


if __name__ == '__main__':
    sys.exit(main())
