import os
import matplotlib.pyplot as plt


def laguerre_gaussian_beam(l, p, x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    amplitude = np.exp(-r**2) * np.power(r, np.abs(l))
    phase = np.exp(1j * l * theta)
    return amplitude * phase

def generate_oam_image(l, img_size=256, noise_level=0.1):
    x = np.linspace(-5, 5, img_size)
    y = np.linspace(-5, 5, img_size)
    X, Y = np.meshgrid(x, y)
    beam = laguerre_gaussian_beam(l, 0, X, Y)
    intensity = np.abs(beam)**2
    noise = noise_level * np.random.rand(img_size, img_size)
    noisy_intensity = intensity + noise
    return noisy_intensity

# Set parameters
img_size = 256
num_modes = 10  # Number of different OAM modes
num_images_per_mode = 100  # Number of images per OAM mode
output_dir = '/content/drive/MyDrive/oam_dataset'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate and save images
for l in range(-num_modes//2, num_modes//2):
    mode_dir = os.path.join(output_dir, f'mode_{l}')
    if not os.path.exists(mode_dir):
        os.makedirs(mode_dir)
    for img_num in range(num_images_per_mode):
        img = generate_oam_image(l, img_size)
        img_path = os.path.join(mode_dir, f'oam_mode_{l}_img_{img_num}.png')
        plt.imsave(img_path, img, cmap='gray')

print("Dataset generation complete.")

# Visualize a few images from each mode
fig, axes = plt.subplots(2, num_modes, figsize=(15, 6))
axes = axes.flatten()

for idx, l in enumerate(range(-num_modes//2, num_modes//2)):
    img_path = os.path.join(output_dir, f'mode_{l}', f'oam_mode_{l}_img_0.png')
    img = plt.imread(img_path)
    axes[idx].imshow(img, cmap='gray')
    axes[idx].set_title(f'OAM Mode l={l}')
    axes[idx].axis('off')

plt.tight_layout()
plt.show()
