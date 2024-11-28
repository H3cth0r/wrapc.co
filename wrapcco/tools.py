from typing import List
from .wrapper import Wrapper

def wrapcco_setup(wrappers: List[Wrapper]) -> None:
    for wrapper in wrappers: wrapper.generate()

# Don't forget to add a function to "clean --all"
