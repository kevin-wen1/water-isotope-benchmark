# Model assets

The model identities follow the 14 October 2026 manuscript. `registry.json` records each checkpoint and whether its weight file is bundled.

| Model | Checkpoint / implementation | Bundled asset |
| --- | --- | --- |
| Adapted DPA4 | strong-rw, `model.ckpt-300.pt`, seeds 1/2/3 | Model description only; weights outside release scope |
| Zero-shot DPA4 | `DPA4-Beta.pt` | [Official model](https://huggingface.co/deepmodelingcommunity/DPA4-Beta) |
| MACE-POLAR | MACE-POLAR-1-M | [Official release](https://github.com/ACEsuit/mace-foundations/releases/tag/mace_polar_1) |
| MACE-OMol | MACE-OMol-0 extra-large-1024 | [Official release](https://github.com/ACEsuit/mace-foundations/releases/tag/mace_omol_0) |
| MB-pol | MBX `single_point` implementation | [MBX](https://github.com/paesanilab/MBX); no learned checkpoint |
| Published NEP-MB-pol | ANN 60 0, cutoff 6/4 Å | `nep.txt` |
| MatterSim | MatterSim-v1.0.0-1M | [Official source](https://github.com/microsoft/mattersim) |
| MACE-MP-0 | MACE-MP-0-medium | [Official source](https://github.com/ACEsuit/mace-mp) |
| CHGNet | CHGNet 0.3.0 | [Official source](https://github.com/CederGroupHub/chgnet) |

## Published NEP checkpoint

The included 113,661-byte weight file was copied from `01-NEP-MB-pol/Train/nep.txt` in the [author release](https://zenodo.org/records/18448848). Its header specifies NEP4, O/H elements, ANN 60 0 and radial/angular cutoffs 6/4 Å. Provenance and the linked paper are recorded in the model's `provenance` entry in `registry.json`.

The manuscript used a single-hidden-layer [NEP CPU implementation](https://github.com/brucefan1983/NEP_CPU). The weight file is an inference input, not a Python package; obtain and build the runtime from its upstream source.

The model release is credited to **Ke Xu**, *Source Code, Compilation, Datasets, Model Training, Testing, and Demos for NEP-MB-pol Water Model*, Zenodo v2, DOI [10.5281/zenodo.18448848](https://doi.org/10.5281/zenodo.18448848), accompanying [Xu et al., NEP-MB-pol](https://doi.org/10.1038/s41524-025-01777-1). The weight file is redistributed unchanged under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). The source archive and member path are recorded in `registry.json`. This attribution does not imply endorsement by the upstream authors.

## Adapted DPA4

The adapted DPA4 seed checkpoints are intentionally outside this release's scope. The registry retains the manuscript's model description with `bundled: false` and `release_required: false`; these checkpoints are not pending release assets. The remaining pretrained models are documented by their version entries.
