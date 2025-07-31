from testbook import testbook

def test_values():
    with testbook('4_scipy_statcs_3d_plots.ipynb', execute=True) as tb:
        # Use value() method to inject code that converts numpy types to Python types
        sigma_value = tb.value('float(sigma[0,0])')
        assert sigma_value == 4.0, f"sigma[0,0]={sigma_value} of task 1.1 is not equal to 4"

        mesgrid_value = tb.value('float(X1[100,100])')
        assert abs(mesgrid_value - 5.0754) <= 0.001, f"X1[100,100]={mesgrid_value} of task 1.2 is not equal to 5.0754"

        Z_value = tb.value('float(max(Z))')
        assert abs(Z_value - 0.00030626) <= 0.0000001, f"max(Z)={Z_value} of task 1.3 is not equal to 0.000306256"