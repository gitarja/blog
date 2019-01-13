FILTER_SIZE = [64, 64, 128, 256]
STRIDE_SIZE = [3, 2, 1]
KERNEL_SIZE = [5, 3, 2]
LATENT_DIM = 32
ENCODED_SHAPE = [5, 25, 128]
POOL_SIZE = 2
STRIDES = 2


# sample rate
HZT = 30
WARM_UP_TIME = 60

#data
T = 200
UNIT = 1
FILE_PATH = "F:\\data\\gait_maturation\\"
BATCH_SIZE = 25
CHECKPOINT_DIR = "F:\\result\\pre-trained\\gait"
CHECKPOINT_PREFIX = "".join([CHECKPOINT_DIR, "ckpt"])
TENSORBOARD_DIR =  "F:\\result\\tensorboard\\gait\\"
LR = 1e-3
NUM_ITER = 1000
MAX_SIG_VAL = 1.9333054193187056
MIN_SIG_VAL = 0.7783509826559956


#discriminator
DISC_DENSE_UNITS = [512, 1024]
DISC_CHECKPOINT_DIR = "F:\\result\\pre-trained\\gait\\disc_raw"
DISC_TENSORBOARD_DIR =  "F:\\result\\tensorboard\\gait\\disc_raw"
TRAIN_FILE_PATH = "".join([FILE_PATH, "data_train.csv"])
TEST_FILE_PATH = "".join([FILE_PATH, "data_test.csv"])
VAL_FILE_PATH = "".join([FILE_PATH, "data_val.csv"])
DIC_LR = 9.5e-3
DIC_NUM_ITER = 500


#plotting
DISC_IMG_LATENT = "F:\\result\\visualization\\gait\\latent"