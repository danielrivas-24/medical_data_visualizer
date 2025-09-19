# test_module.py

import unittest
import medical_data_visualizer
import matplotlib
import pandas as pd
import numpy as np


class MedicalDataVisualizerTestCase(unittest.TestCase):

    def setUp(self):
        self.df = medical_data_visualizer.df

    def test_dataframe_loaded(self):
        """The DataFrame must be loaded correctly with expected columns."""
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertGreater(len(self.df), 0, "The DataFrame is empty.")
        expected_columns = [
            "id", "age", "gender", "height", "weight", "ap_hi",
            "ap_lo", "cholesterol", "gluc", "smoke", "alco",
            "active", "cardio", "overweight"
        ]
        for col in expected_columns:
            self.assertIn(col, self.df.columns, f"Missing column: {col}")

    def test_overweight_column(self):
        """The 'overweight' column should contain only 0 or 1."""
        self.assertTrue(set(self.df["overweight"].unique()).issubset({0, 1}))

    def test_normalize_cholesterol_gluc(self):
        """'cholesterol' and 'gluc' must be normalized to 0 or 1."""
        self.assertTrue(set(self.df["cholesterol"].unique()).issubset({0, 1}))
        self.assertTrue(set(self.df["gluc"].unique()).issubset({0, 1}))

    def test_cat_plot_returns_figure(self):
        """draw_cat_plot should return a Matplotlib Figure object."""
        fig = medical_data_visualizer.draw_cat_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)

    def test_cat_plot_data_structure(self):
        """The cat plot DataFrame must contain all variables with cardio split."""
        df_cat = pd.melt(
            self.df,
            id_vars=['cardio'],
            value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
        )
        grouped = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

        variables = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
        for var in variables:
            subset = grouped[grouped['variable'] == var]
            self.assertIn(0, subset['cardio'].unique(), f"Cardio=0 missing in {var}")
            self.assertIn(1, subset['cardio'].unique(), f"Cardio=1 missing in {var}")
            self.assertIn(0, subset['value'].unique(), f"Value=0 missing in {var}")
            self.assertIn(1, subset['value'].unique(), f"Value=1 missing in {var}")

    def test_heat_map_returns_figure(self):
        """draw_heat_map should return a Matplotlib Figure object."""
        fig = medical_data_visualizer.draw_heat_map()
        self.assertIsInstance(fig, matplotlib.figure.Figure)

    def test_heat_map_correlation_matrix(self):
        """The correlation matrix must be square and symmetric."""
        df_heat = self.df.copy()
        # Apply cleaning filters
        df_heat = df_heat[df_heat['ap_lo'] <= df_heat['ap_hi']]
        h_low = df_heat['height'].quantile(0.025)
        h_high = df_heat['height'].quantile(0.975)
        df_heat = df_heat[(df_heat['height'] >= h_low) & (df_heat['height'] <= h_high)]
        w_low = df_heat['weight'].quantile(0.025)
        w_high = df_heat['weight'].quantile(0.975)
        df_heat = df_heat[(df_heat['weight'] >= w_low) & (df_heat['weight'] <= w_high)]

        corr = df_heat.corr()
        self.assertEqual(corr.shape[0], corr.shape[1], "The correlation matrix is not square.")
        self.assertTrue(np.allclose(corr, corr.T, atol=1e-8), "The correlation matrix is not symmetric.")


if __name__ == "__main__":
    unittest.main()