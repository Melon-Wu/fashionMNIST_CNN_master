# fashionMNIST_CNN

## CNN模型

# ![CNN Model](E:\ML\Pictures\fashionMNIST_CNN\CNN.png)

## 模型参数

![Summary](E:\ML\Pictures\fashionMNIST_CNN\CNN_summary.png)

## 优化函数

```
SGD + Nesterov Momentum
```

## 模型准确率

| 训练集准确率            | 验证集准确率             | 测试集准确率            |
| ----------------------- | ------------------------ | ----------------------- |
| <center>93.01%</center> | <center>93.04%</center>> | <center>93.75%</center> |

## 模型训练

```python
CUDA_VISIBLE_DEVICE=0 python train.py
```

**CUDA_VISIBLE_DEVICE**对应显卡序号：

```python
nvidia-smi
```

训练时会自动保存验证集准确率较高的pth文件，以供测试

## 模型测试

由于本数据集没有区分测试集和验证集，故使用随机从测试集中每次迭代取batch_size的样本作为验证集，方便训练过程调整超参数

将测试集中的PATH改为对应保存的pth文件即可

```
CUDA_VISIBLE_DEVICE=0 python test.py
```

## TO DO

- [ ] readme.md in English

## 参考

[ashmeet13]: https://github.com/ashmeet13/FashionMNIST-CNN
