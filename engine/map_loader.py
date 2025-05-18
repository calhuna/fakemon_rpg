def load_map(filepath):
    with open(filepath) as f:
        return [list(line.strip()) for line in f]