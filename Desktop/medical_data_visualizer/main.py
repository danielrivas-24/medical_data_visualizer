# main.py

import matplotlib.pyplot as plt
import medical_data_visualizer
import unittest
import test_module

# Run functions and show/save figures
if __name__ == "__main__":
    # Categorical plot
    fig1 = medical_data_visualizer.draw_cat_plot()
    fig1.savefig("catplot.png")
    print("Categorical plot saved as catplot.png")
    plt.close(fig1)

    # Heatmap
    fig2 = medical_data_visualizer.draw_heat_map()
    fig2.savefig("heatmap.png")
    print("Heatmap saved as heatmap.png")
    plt.close(fig2)

    # Run tests
    print("\nRunning unit tests...\n")
    unittest.main(module=test_module, exit=False)