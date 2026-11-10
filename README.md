# Aquiles LED board review

Editable KiCad reference for the eight-LED board from Aquiles, with a
reproducible design-rule and electrical-rule review.

**PCB and schematic design** · Misael Castillo ([@misaacastillo](https://github.com/misaacastillo)).

The board, schematic and project in `board/` are byte-for-byte copies of
the corresponding files in the [public Aquiles snapshot](https://github.com/ZaCoso/Aquiles_Project/tree/a3d2e4bdd83270054a9b82539448bb7960d39b9d/hardware/placa_leds).
This repository adds the standalone review workflow and documentation.
The MIT notice distributed with the source is preserved in [LICENSE](LICENSE).

## Inspect the design

Open `board/Leds aquiles.kicad_pro` in KiCad 9 or later. The board contains
eight LEDs, eight resistors and one two-pin connector. The schematic has
generic LED and resistor values. Selecting those parts, checking the supply
and current, and validating the assembled board are separate tasks.

## Reproduce the review

With KiCad 9.0.9 and Python 3 installed, initialize the default symbol and
footprint libraries in KiCad. Then run these commands from the repo root.

```sh
./scripts/check.sh
python3 scripts/summarize.py
```

GitHub Actions runs the checks with the pinned
[official KiCad image](https://www.kicad.org/download/docker/) and saves the
JSON reports and summary as a workflow artifact. A successful workflow
means KiCad generated and the script parsed both reports. Review the
reported findings for the design's status. A physical and component-value
review remains pending.

This release contains the design sources and review files. The workflow
produces review reports rather than fabrication files.
