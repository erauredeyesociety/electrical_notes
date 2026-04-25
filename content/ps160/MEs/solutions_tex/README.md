# PS160 ME Solutions — LaTeX versions

These `.tex` files are Overleaf-ready versions of the ME walkthroughs in `../solutions/`. Each file is a complete, standalone document — paste into Overleaf and compile.

## Files

| .tex | Topic | Source key verified? |
|------|-------|----------------------|
| ME12_v1_solutions.tex | Fluid Mechanics | ✓ |
| ME14_v1_solutions.tex | Oscillations | ✓ |
| ME15_v1_solutions.tex | Waves | ✓ |
| ME16_v1_solutions.tex | Sound | ✓ |
| ME17_v1_solutions.tex | Temperature & Expansion | ✓ |
| ME18_v1_solutions.tex | Kinetic Theory | ✓ |
| ME19_v1_solutions.tex | Thermo Processes | ✓ |
| ME20_v1_solutions.tex | Engines & Entropy | ✓ |
| ME33_v1_solutions.tex | Geometric Optics | ✗ (no key, independently solved) |
| ME34_v1_solutions.tex | Mirrors & Lenses | ✗ |
| ME35-36_v1_solutions.tex | Interference & Diffraction | ✗ |

## Packages

Each file uses only standard packages (built into Overleaf's TeX Live):
- `geometry` (1-inch margins)
- `amsmath`, `amssymb`
- `enumitem`

ME12 also uses `siunitx`, `hyperref`, `xcolor` (all standard in Overleaf).

## How to use in Overleaf

1. Create a new project (or open existing).
2. Copy the entire `.tex` file contents into the editor.
3. Compile — the document is self-contained; no `\input` or external resources needed.

## Notes

- Markdown versions live in `../solutions/` if you prefer to read in VSCode.
- Image-dependent items (PV diagrams, two-mirror geometry, contact lens) are flagged with `\warn` in the .tex.
