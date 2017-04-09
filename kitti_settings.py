import datetime
# Where KITTI data will be saved if you run process_kitti.py
# If you directly download the processed data, change to the path of the data.
dtnow = datetime.now()
# Do not change this
DATA_DIR = './kitti_data/'

# Where model weights and config will be saved if you run kitti_train.py
# If you directly download the trained weights, change to appropriate path.
WEIGHTS_DIR = './model_data/{}-{}-{}-{}-{}/'.format(dtnow.year, dtnow.month, dtnow.hour, dtnow.minute, dtnow.second)

# Where results (prediction plots and evaluation file) will be saved.
RESULTS_SAVE_DIR = './kitti_results/{}-{}-{}-{}-{}/'.format(dtnow.year, dtnow.month, dtnow.hour, dtnow.minute, dtnow.second)
