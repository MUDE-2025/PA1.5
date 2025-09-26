from testbook import testbook
import numpy as np

def test_values():
    with testbook('3_scipy_statcs_3d_plots.ipynb', execute=True) as tb:
        # Use value() method to inject code that converts numpy types to Python types
        sigma_value = tb.value('float(sigma[0,0])')
        assert np.isclose(sigma_value, 4.0, atol=1e-6), f"sigma[0,0]={sigma_value} of task 1.1 is not equal to 4"

        mesgrid_value = tb.value('float(X1[100,100])')
        assert np.isclose(mesgrid_value, 8.8442, atol=1e-3), f"X1[100,100]={mesgrid_value} of task 1.2 is not equal to 8.8442"

        Z_value = tb.value('float(max(Z))')
        assert np.isclose(Z_value, 0.00030627, atol=1e-7), f"max(Z)={Z_value} of task 1.3 is not equal to 0.00030627"
