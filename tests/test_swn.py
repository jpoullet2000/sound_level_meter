from slm.swn import Swn

class TestSwn():

    def test_swn_to_df(self):
        swn_file = 'swn/DATA0025.SWN'
        swno = Swn(swn_filename=swn_file)
        assert swno.df.shape[1] == 7

    def test_plot(self):
        swn_file = 'swn/DATA0025.SWN'
        swno = Swn(swn_filename=swn_file)
        p = swno.plot()