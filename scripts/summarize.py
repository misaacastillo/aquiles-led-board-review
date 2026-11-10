from collections import Counter
import json
from pathlib import Path

reports = Path("reports")
drc = json.loads((reports / "drc.json").read_text())
erc = json.loads((reports / "erc.json").read_text())

print(f"KiCad version: {(reports / 'kicad-version.txt').read_text().strip()}")
checks = {
    "DRC": drc["violations"] + drc["unconnected_items"],
    "ERC": [item for sheet in erc["sheets"] for item in sheet["violations"]],
}
for name, findings in checks.items():
    counts = Counter((item["severity"], item["type"]) for item in findings)
    print(f"{name}: {len(findings)} findings")
    for (severity, kind), count in sorted(counts.items()):
        print(f"  {severity} {kind}: {count}")
