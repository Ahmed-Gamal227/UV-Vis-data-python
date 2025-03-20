import numpy as np
import matplotlib.pyplot as plt

# Function to load data from a text file
def load_uv_vis_data(file_path):
    """
    Load UV-Vis spectra data from a text file.

    Parameters:
    - file_path: Path to the text file.

    Returns:
    - wavelengths: Array of wavelengths (nm).
    - absorbance: Array of absorbance values.
    """
    try:
        
        data = np.loadtxt(file_path, delimiter=None)
        wavelengths = data[:, 0]  # First column: Wavelengths (nm)
        absorbance = data[:, 1]   # Second column: ABS/Intensity (a.u)
        return wavelengths, absorbance
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None


def plot_uv_vis_spectrum(wavelengths, absorbance, title="UV-Vis Spectrum"):
    """
    Plot the UV-Vis spectrum.

    Parameters:
    - wavelengths: Array of wavelengths (nm).
    - absorbance: Array of absorbance values.
    - title: Title of the plot (default: "UV-Vis Spectrum").
    """
    plt.figure(figsize=(8, 5))
    plt.plot(wavelengths, absorbance, color="blue", label="Absorbance")
    plt.title(title)
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Absorbance")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.show()

# Main program
if __name__ == "__main__":
    
    file_path = "ZnO.txt"
    wavelengths, absorbance = load_uv_vis_data(file_path)
    
    if wavelengths is not None and absorbance is not None:
        plot_uv_vis_spectrum(wavelengths, absorbance)
    else:
        print("Unable to plot spectrum due to data loading error.")
