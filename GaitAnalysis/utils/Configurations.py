FILTER_SIZE = [32, 32, 64, 128]
STRIDE_SIZE = [3, 2, 1]
KERNEL_SIZE = [5, 3, 2]
LATENT_DIM = 16
ENCODED_SHAPE = [5, 25, 128]
POOL_SIZE = 2
STRIDES = 2


# sample rate
HZT = 300
WARM_UP_TIME = 60

#data
T = 200
UNIT = 1
FILE_PATH = "F:\\data\\gait_maturation\\"
BATCH_SIZE = 25
CHECKPOINT_DIR = "F:\\result\\pre-trained\\gait\\"
CHECKPOINT_PREFIX = "".join([CHECKPOINT_DIR, "ckpt"])
TENSORBOARD_DIR =  "F:\\result\\tensorboard\\gait\\"
LR = 1e-3
NUM_ITER = 1000
