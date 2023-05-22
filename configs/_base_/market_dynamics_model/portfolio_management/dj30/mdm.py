market_dynamics_model = dict(
    data_path='data/portfolio_management/dj30/DJI.csv',
fitting_parameters=['1','2','4'],
labeling_parameters=[-0.25,0.25],
dynamic_number=3,
length_limit=24,
OE_BTC=False,
PM="data/portfolio_management/dj30/test.csv",
process_datafile_path='',
market_dynamic_labeling_visualization_paths='',
key_indicator='adjcp',
timestamp='date',
tic='tic',
mode='slope',
hard_length_limit=-1,
slope_mdd_threshold=0.01
)