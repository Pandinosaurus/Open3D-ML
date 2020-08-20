import tensorflow as tf

# there should be pipeline. pipeline is bigger that randlanet
from ml3d.datasets import Toronto3D
from ml3d.tf.models import KPFCNN
from ml3d.tf.datasets import TF_Dataset
from ml3d.torch.utils import Config
from os.path import abspath, dirname

# from tf2torch import load_tf_weights

config = dirname(abspath(__file__)) + '/../ml3d/torch/configs/kpconv_toronto3d.py'
cfg = Config.load_from_file(config)

dataset = Toronto3D(cfg.dataset)
model = KPFCNN(cfg.model)
print(model)
# pipeline = SemanticSegmentation(model, dataset, cfg.pipeline)

# device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
# device     = torch.device('cpu')

# pipeline.run_train(device)

tf_data = TF_Dataset(dataset = dataset.get_split('training'), model = model)
loader = tf_data.get_loader()
# print(loader)
for data in loader:
#     # print(data)
    model(data)
    # for a in data:
#         print(a.shape)
    break
