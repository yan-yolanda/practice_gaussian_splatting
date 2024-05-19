import argparse #导入进行参数处理的包
import json #导入处理json文件的包，有一部分参数存储在json文件中

#创建参数总容器
parser = argparse.ArgumentParser()
file = "config.json"

#打开json文件
with open(file,'r') as f:
    file_args = json.load(f)

#添加json文件中的参数
for arg in file_args:
    parser.add_argument("--"+arg,default=file_args[arg])

#手动设置一些参数
parser.add_argument("--detect_anomaly", action="store_true", default=False)
parser.add_argument("--test_iterations", nargs="+", type=int, default=[100,1_000, 7_000, 30_000])
parser.add_argument("--save_iterations", nargs="+", type=int, default=[100,1_000, 7_000, 30_000])    
parser.add_argument("--checkpoint_iterations", nargs="+", type=int, default=[100, 1_000, 7_000, 30_000])
parser.add_argument("--start_checkpoint", type=str, default = None)

#解析参数
args = parser.parse_args(args=[])

#打印参数
for k in args.__dict__:
    print(k + ": " + str(args.__dict__[k]))

if __name__ == '__main__':

    # 参数处理
    config = parser.parse_args()

    # # 数据读取
    # train_data = GSDataLoader(data_path)

    # # 模型生成
    # gaussian = GaussianModel(config, train_data)

    # # 训练器
    # trainer = GSTrainer(gaussian)
    
    # # 开始训练
    # trainer.train()



