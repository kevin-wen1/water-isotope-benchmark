# Paired-Isotopologue Water Dataset and Models

[中文说明](README.zh-CN.md)

Complete DFT reference data and model information accompanying *Paired-Isotopologue Hessian Benchmarking for Second-Order Validation of Machine-Learned Water Potentials*, aligned with the manuscript and Supporting Information dated 14 October 2026.

## Dataset

All **5100 geometries** are included. Each compressed NPZ file contains atomic numbers, Cartesian coordinates, DFT energy, forces, gradient, the full Cartesian Hessian, target O–H atom indices and HH/DH/DD mass assignments.

| Split | Geometries | Reference files |
| --- | ---: | --- |
| Training | 3000 | `data/train/` |
| Validation | 1000 | `data/validation/` |
| Primary test | 1000 | `data/primary_test/` |
| External test | 100 | `data/external_test/` |

The primary collection comes from one VASP AIMD trajectory and is split by central-water hydrogen-bond count: 0–2 / 3 / 4. The external collection comes from a separate MACE-driven trajectory and contains 100 geometries from 48 parent frames. The DFT reference is Gaussian 16 A.03, ωB97X-D/6-31+G(d,p), evaluated at fixed sampled geometries without optimization.

The two test sets also include **6600 target frequencies and participation values** and **4400 paired isotope shifts** in `data/isotope_reference.csv` and `data/isotope_shifts.csv`. HH, DH and DD share the same geometry and electronic Hessian; the target O–H remains protiated. See [data/README.md](data/README.md) for definitions, units and selection rules.

## Read the data

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
    masses = ref["masses_amu"]  # target arm × HH/DH/DD × atom
```

Split IDs are in `data/splits/`; external parent-frame information is in `data/external100_geom.csv`. Dataset metadata are in [dataset.json](data/dataset.json).

## Models

The included [NEP weight file](models/nep.txt) is the author's published **NEP4 ANN 60 0 model with 6/4 Å cutoffs**. [models/README.md](models/README.md) and [registry.json](models/registry.json) record the manuscript's model versions, official sources and NEP attribution. Other pretrained weights can be obtained from their linked upstream sources. Adapted DPA4 seed checkpoints are outside this release's scope.

This repository contains reference data, model information and a data reader. Model predictions, error summaries and manuscript figures are not included.

## Citation and licensing

Citation metadata are provided in [CITATION.cff](CITATION.cff). The unchanged third-party NEP checkpoint is distributed under its upstream [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/); attribution is in [models/README.md](models/README.md). A reuse license for the original benchmark dataset and helper code has not yet been specified.
