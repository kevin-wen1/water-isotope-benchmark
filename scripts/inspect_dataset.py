"""Read reference archives and show their fields; no model evaluation is run."""
import argparse
from pathlib import Path

import numpy as np


def inspect(path, verbose=True):
    with np.load(path, allow_pickle=False) as archive:
        arrays = {name: archive[name] for name in archive.files}
    n = len(arrays["atomic_numbers"])
    shapes = {"positions_angstrom": (n, 3), "forces_eV_A": (n, 3),
              "gradient_eV_A": (n, 3), "hessian_sym_eVA2": (3*n, 3*n),
              "target_O_indices": (2,), "target_H_indices": (2,), "masses_amu": (2, 3, n)}
    for name, shape in shapes.items():
        if arrays[name].shape != shape or not np.isfinite(arrays[name]).all():
            raise ValueError(f"Invalid {name} in {path}")
    if arrays["energy_eV"].size != 1 or not np.isfinite(arrays["energy_eV"]).all():
        raise ValueError(f"Invalid reference energy in {path}")
    if not np.allclose(arrays["forces_eV_A"], -arrays["gradient_eV_A"], atol=1e-12, rtol=0):
        raise ValueError(f"Inconsistent force/gradient signs in {path}")
    if not np.allclose(arrays["hessian_sym_eVA2"], arrays["hessian_sym_eVA2"].T, atol=1e-9, rtol=1e-9):
        raise ValueError(f"Asymmetric reference Hessian in {path}")
    if verbose:
        print(f"{path.name}: {n} atoms")
        for name, array in arrays.items():
            print(f"  {name}: shape={array.shape}, dtype={array.dtype}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1] / "data/primary_test/4-HB-745.npz")
    parser.add_argument("--summary", action="store_true", help="Validate all archives and print only a count")
    args = parser.parse_args()
    paths = sorted(args.path.rglob("*.npz")) if args.path.is_dir() else [args.path]
    if not paths:
        parser.error("No reference NPZ files found")
    for path in paths:
        inspect(path, verbose=not args.summary)
    if args.summary:
        print(f"Validated {len(paths)} reference archives")


if __name__ == "__main__":
    main()
