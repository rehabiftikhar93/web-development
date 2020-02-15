from pathlib import Path


path=Path()
for function in path.glob("*.txt"):
    print(function)
