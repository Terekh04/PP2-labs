import os

def task(path):
    if os.path.exists(path):
        print(f'Path {path} exists')
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f'Path {path} does not exists')