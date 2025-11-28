import matplotlib.pyplot as plt

def create_barchart(data, labels, title="Bar Chart", xlabel="Categories", ylabel="Values"):
    
    plt.figure(figsize=(10, 6))
    plt.bar(labels, data, color='skyblue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()