# 配对同位素水数据集与模型

按 **2026 年 10 月 14 日新版正文和 SI** 整理，包含完整 DFT 参考数据、模型信息和数据读取脚本。

## 数据内容

全部 **5100 个构型**均已包含。每个 `.npz` 文件保存原子种类、坐标、DFT 能量、力、梯度、完整 Cartesian Hessian、目标 O–H 原子索引及 HH/DH/DD 质量配置。

| 划分 | 构型数 | 目录 |
| --- | ---: | --- |
| 训练集 | 3000 | `data/train/` |
| 验证集 | 1000 | `data/validation/` |
| 主测试集 | 1000 | `data/primary_test/` |
| 外部测试集 | 100 | `data/external_test/` |

主数据集来自同一条 VASP AIMD 轨迹，按中心水的氢键数 0–2 / 3 / 4 划分。外部集来自独立的 MACE 驱动轨迹，100 个构型对应 48 个母帧。参考计算采用 Gaussian 16 A.03、ωB97X-D/6-31+G(d,p)，在采样构型上直接计算，不做几何优化。

两个测试集还提供 **6600 条 DFT 目标频率与参与度**、**4400 条配对同位素频移**，分别保存在 `data/isotope_reference.csv` 和 `data/isotope_shifts.csv`。HH、DH、DD 共用坐标和电子 Hessian，目标 O–H 的 H 始终保持为氕。字段、单位与选模定义见 [data/README.md](data/README.md)。

## 读取数据

```bash
git clone https://github.com/kevin-wen1/water-isotope-benchmark.git
cd water-isotope-benchmark
python -m pip install -r requirements.txt
python scripts/inspect_dataset.py
python scripts/inspect_dataset.py data --summary
```

```python
import numpy as np

with np.load("data/primary_test/4-HB-745.npz", allow_pickle=False) as ref:
    positions = ref["positions_angstrom"]
    hessian = ref["hessian_sym_eVA2"]
    masses = ref["masses_amu"]  # 目标 O–H × HH/DH/DD × 原子
```

固定划分 ID 位于 `data/splits/`，外部构型母帧信息位于 `data/external100_geom.csv`，数据版本和覆盖情况见 [dataset.json](data/dataset.json)。

## 模型

仓库仅记录与论文对应的模型名称、版本和官方获取地址，见 [模型说明](models/README.md) 和 [registry.json](models/registry.json)，不存放第三方模型权重。NEP-MB-pol 指作者正式发布的 **NEP4、ANN 60 0、6/4 Å 截断**模型。本次不提供 adapted DPA4 各 seed 的权重。

仓库不包含模型预测、误差汇总或论文结果图。引用信息见 [CITATION.cff](CITATION.cff)。本项目原创数据及读取脚本的再使用许可尚未指定；第三方模型按各自官方来源的许可获取。
