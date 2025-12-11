def read_file_stats(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        lines = content.split('\n')
        words = content.split()
        chars = len(content)
        return {
            "lines": len(lines),
            "words": len(words),
            "characters": chars
        }
    except FileNotFoundError:
        return "File not found"

def grep_file(filename, pattern):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if pattern.lower() in line.lower()]
    except FileNotFoundError:
        return "File not found"

if __name__ == "__main__":
    stats = read_file_stats("requirements.txt")
    print(f"Stats: {stats}")