#!/bin/sh
set -eu

cd "$(dirname "$0")/.."
export LC_ALL=C
kicad_cli="${KICAD_CLI:-kicad-cli}"

mkdir -p reports
"$kicad_cli" version > reports/kicad-version.txt
"$kicad_cli" pcb drc --format json --output reports/drc.json 'board/Leds aquiles.kicad_pcb'
"$kicad_cli" sch erc --format json --output reports/erc.json 'board/Leds aquiles.kicad_sch'
test -s reports/drc.json
test -s reports/erc.json
