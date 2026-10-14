# Reference dataset

## Collection and split

The primary 5000 water-cluster geometries come from one VASP AIMD trajectory. Central-water hydrogen-bond counts 0–2, 3 and 4 define the 3000 training, 1000 validation and 1000 primary-test geometries. Every target arm and isotope variant stays with its geometry. Fixed observed IDs are in `splits/`.

The independent-source collection contains 100 geometries from a separate MACE-driven water trajectory. `external100_geom.csv` records the 48 parent-frame IDs, center-water IDs and structural metadata.

Gaussian 16 A.03 reference calculations use `wb97xd/6-31+G(d,p) freq nosymm` at the sampled geometries, without optimization.

## One NPZ per geometry

| Field | Shape | Unit / definition |
| --- | --- | --- |
| `atomic_numbers` | `(N,)` | O = 8, H = 1 |
| `positions_angstrom` | `(N, 3)` | Å |
| `energy_eV` | scalar | eV, reference electronic energy |
| `forces_eV_A` | `(N, 3)` | eV/Å, negative energy gradient |
| `gradient_eV_A` | `(N, 3)` | eV/Å, energy gradient |
| `hessian_sym_eVA2` | `(3N, 3N)` | eV/Å², reference Cartesian Hessian |
| `target_O_indices` | `(2,)` | Zero-based oxygen indices for two target arms |
| `target_H_indices` | `(2,)` | Zero-based indices of the two target hydrogens |
| `masses_amu` | `(2, 3, N)` | Target arm × HH/DH/DD pattern × atom, u |

HH uses H throughout. DH deuterates the non-target H of the target water. DD additionally deuterates environmental H atoms. The selected target O–H remains protiated throughout. The electronic labels and coordinates are shared by all mass patterns. Exact masses are in `dataset.json`.

Load archives with `numpy.load(path, allow_pickle=False)`. Atom ordering must be preserved across every field. Files are stored as `<split>/<geometry_id>.npz`, where split is `train`, `validation`, `primary_test` or `external_test`. For example, `primary_test/4-HB-745.npz` contains an 18-atom primary-test geometry. Hessian row and column indices follow the flattened Cartesian ordering x₀, y₀, z₀, x₁, y₁, z₁, … .

## Isotope reference labels

The two CSV files provide DFT standard answers for the 1000 primary-test and 100 external-test geometries. Rows are identified by `split`, `geometry_id` and `arm`. Arm 0 or 1 indexes the corresponding entry in `target_O_indices` and `target_H_indices` of the reference archive. `isotope` identifies the HH, DH or DD mass assignment for that arm.

| File / value field | Definition | Coverage |
| --- | --- | --- |
| `isotope_reference.csv` / `reference_target_frequency_cm1` | Independently selected positive-curvature target-mode frequency, cm⁻¹ | 6600 rows: 6000 primary + 600 external |
| `isotope_reference.csv` / `reference_target_participation` | Raw squared projection of the selected Cartesian-normalized mode onto the target O–H stretching coordinate, dimensionless | 6600 rows: 6000 primary + 600 external |
| `isotope_shifts.csv` / `reference_shift_cm1` | Endpoint frequency difference, cm⁻¹; `HH_to_DH` = DH − HH and `DH_to_DD` = DD − DH | 4400 rows: 4000 primary + 400 external |

For each mass assignment, rebuild the mass-weighted translation/rotation subspace and project it out before diagonalizing the mass-weighted Cartesian Hessian. For a nonlinear cluster this leaves 3N − 6 internal modes. Convert each mass-weighted eigenvector back to Cartesian coordinates and normalize it to unit Euclidean norm. The target stretching vector has equal and opposite unit-bond-direction components on H and O, each scaled by 1/√2. Participation is the squared scalar product with this vector; it is not normalized by the sum over modes. Select the mode with maximum participation among positive-curvature modes, separately at every isotope endpoint. The eigenvalue-to-frequency conversion factor is 521.4708983725064 cm⁻¹ for eigenvalues in eV/(Å²·u).

These tables contain selected target-mode labels, not complete spectra or eigenvectors. The shifts use independently selected endpoint modes; they do not assert a continuously tracked mode identity. All frequency and participation cells are populated. Training and validation isotope labels are not included in these tables.

## Availability

All 5100 reference archives, fixed split lists and external-source metadata are included. Both test sets have complete target-frequency, participation and paired-shift tables. `dataset.json` records the coverage and path pattern for each split. The primary reference coordinates, energy, force signs and Hessians were checked against the actual 3000/1000/1000 training/validation/test inputs. Test-set target frequencies and participation were checked against the current mass-specific projection convention.
