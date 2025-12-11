import json

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def filter_json(data, key, value):
    return [item for item in data if item.get(key) == value]

if __name__ == "__main__":
    sample = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
    save_json("sample.json", sample)
    loaded = load_json("sample.json")
    print(loaded)