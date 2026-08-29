import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],

    "age": [20, 25, 22, 30, 24],
    
    "score": [85, 72, 91, 68, 88]
}

df = pd.DataFrame(data)

print(df)