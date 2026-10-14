# Models used in the benchmark

Model versions follow the 14 October 2026 manuscript. This directory contains model descriptions and official source links. Model weights are not bundled.

| Model | Checkpoint / implementation | Official source |
| --- | --- | --- |
| Adapted DPA4 | strong-rw, `model.ckpt-300.pt`, seeds 1/2/3 | Model description only; seed weights outside release scope |
| Zero-shot DPA4 | `DPA4-Beta.pt` | [DPA4-Beta](https://huggingface.co/deepmodelingcommunity/DPA4-Beta) |
| MACE-POLAR | MACE-POLAR-1-M | [Author release](https://github.com/ACEsuit/mace-foundations/releases/tag/mace_polar_1) |
| MACE-OMol | MACE-OMol-0 extra-large-1024 | [Author release](https://github.com/ACEsuit/mace-foundations/releases/tag/mace_omol_0) |
| MB-pol | MBX `single_point` implementation | [MBX](https://github.com/paesanilab/MBX) |
| Published NEP-MB-pol | NEP4, O/H, ANN 60 0, radial/angular cutoffs 6/4 Å | [Author release, Zenodo v2](https://zenodo.org/records/18448848) |
| MatterSim | MatterSim-v1.0.0-1M | [MatterSim](https://github.com/microsoft/mattersim) |
| MACE-MP-0 | MACE-MP-0-medium | [MACE foundation models](https://github.com/ACEsuit/mace-mp) |
| CHGNet | CHGNet 0.3.0 | [CHGNet](https://github.com/CederGroupHub/chgnet) |

For NEP-MB-pol, the specific author-release file is `01-NEP-MB-pol/Train/nep.txt` in `01-NEP-MB-pol.zip`, associated with [Xu et al., NEP-MB-pol](https://doi.org/10.1038/s41524-025-01777-1). The manuscript used the single-hidden-layer [NEP CPU implementation](https://github.com/brucefan1983/NEP_CPU). Additional architecture and source details are recorded in [registry.json](registry.json).
