import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. Basic Line Plot
# ==========================================

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('Basic Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# ==========================================
# 2. Multiple Lines in One Plot
# ==========================================

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linewidth=2, linestyle='--')
plt.title('Sine and Cosine Functions')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# ==========================================
# 3. Scatter Plot
# ==========================================

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.colorbar(label='Color Value')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# ==========================================
# 4. Bar Chart
# ==========================================

categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue', edgecolor='black')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Horizontal bar chart
plt.figure(figsize=(8, 6))
plt.barh(categories, values, color='coral', edgecolor='black')
plt.title('Horizontal Bar Chart')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.show()

# ==========================================
# 5. Histogram
# ==========================================

data = np.random.randn(1000)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='green', alpha=0.7, edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.show()

# ==========================================
# 6. Pie Chart
# ==========================================

sizes = [30, 25, 20, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']
colors = ['gold', 'lightblue', 'lightgreen', 'pink', 'lightyellow']
explode = (0.1, 0, 0, 0, 0)  # Explode first slice

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, 
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Pie Chart')
plt.axis('equal')  # Equal aspect ratio
plt.show()

# ==========================================
# 7. Subplots
# ==========================================

x = np.linspace(0, 10, 100)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1
axes[0, 0].plot(x, np.sin(x), 'r')
axes[0, 0].set_title('Sine')
axes[0, 0].grid(True)

# Plot 2
axes[0, 1].plot(x, np.cos(x), 'b')
axes[0, 1].set_title('Cosine')
axes[0, 1].grid(True)

# Plot 3
axes[1, 0].plot(x, np.tan(x), 'g')
axes[1, 0].set_title('Tangent')
axes[1, 0].set_ylim(-5, 5)
axes[1, 0].grid(True)

# Plot 4
axes[1, 1].plot(x, x**2, 'purple')
axes[1, 1].set_title('Quadratic')
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()

# ==========================================
# 8. Box Plot
# ==========================================

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.figure(figsize=(8, 6))
plt.boxplot(data, labels=['Group 1', 'Group 2', 'Group 3'])
plt.title('Box Plot')
plt.ylabel('Values')
plt.grid(True, alpha=0.3)
plt.show()

# ==========================================
# 9. Area Plot
# ==========================================

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.fill_between(x, y1, alpha=0.5, label='sin(x)')
plt.fill_between(x, y2, alpha=0.5, label='cos(x)')
plt.title('Area Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# ==========================================
# 10. Contour Plot
# ==========================================

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.figure(figsize=(10, 8))
contour = plt.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(contour, label='Z value')
plt.title('Contour Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# ==========================================
# 11. Heatmap
# ==========================================

data = np.random.rand(10, 10)

plt.figure(figsize=(8, 6))
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar(label='Value')
plt.title('Heatmap')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# ==========================================
# 12. 3D Plot
# ==========================================

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Data
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

ax.scatter(x, y, z, c=z, cmap='viridis', marker='o', s=50)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Scatter Plot')
plt.show()

# ==========================================
# 13. Customizing Plot Styles
# ==========================================

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))

# Different line styles and markers
plt.plot(x, y, color='#FF5733', linewidth=3, linestyle='-', 
         marker='o', markersize=5, markevery=10, 
         label='Custom Style', alpha=0.7)

plt.title('Customized Plot', fontsize=16, fontweight='bold')
plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.5)
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)
plt.show()

# ==========================================
# 14. Stacked Bar Chart
# ==========================================

categories = ['A', 'B', 'C', 'D']
values1 = [20, 35, 30, 35]
values2 = [25, 32, 34, 20]
values3 = [10, 15, 20, 25]

x_pos = np.arange(len(categories))

plt.figure(figsize=(10, 6))
plt.bar(x_pos, values1, label='Group 1', color='skyblue')
plt.bar(x_pos, values2, bottom=values1, label='Group 2', color='orange')
plt.bar(x_pos, values3, bottom=np.array(values1)+np.array(values2), 
        label='Group 3', color='green')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Stacked Bar Chart')
plt.xticks(x_pos, categories)
plt.legend()
plt.show()

# ==========================================
# 15. Saving Plots
# ==========================================

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('Plot to Save')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

# Save in different formats
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.savefig('plot.pdf', bbox_inches='tight')
plt.savefig('plot.jpg', dpi=150, bbox_inches='tight')
print("Plots saved as PNG, PDF, and JPG")
plt.show()

# ==========================================
# 16. Error Bars
# ==========================================

x = np.arange(0, 10, 1)
y = x ** 2
error = np.random.rand(10) * 10

plt.figure(figsize=(8, 6))
plt.errorbar(x, y, yerr=error, fmt='o-', capsize=5, 
             capthick=2, label='Data with error')
plt.title('Error Bar Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# ==========================================
# 17. Polar Plot
# ==========================================

theta = np.linspace(0, 2*np.pi, 100)
r = np.abs(np.sin(3*theta))

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, linewidth=2)
ax.set_title('Polar Plot')
plt.show()

# ==========================================
# 18. Different Plot Styles
# ==========================================

print("Available styles:", plt.style.available)

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Using different styles
styles = ['default', 'ggplot', 'seaborn-v0_8', 'classic']

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for i, style in enumerate(styles[:4]):
    plt.style.use(style)
    axes[i].plot(x, y)
    axes[i].set_title(f'Style: {style}')
    axes[i].grid(True)

plt.tight_layout()
plt.show()

# Reset to default style
plt.style.use('default')