import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "cadquery"))

from common.parameters import *
from common.exporter import export_part
from common.geometry import create_plate, add_holes


def make_part():
    part = create_plate(MACHINE_LENGTH, 40, BASE_THICKNESS, FILLET_SMALL)

    x = MACHINE_LENGTH / 2 - 25
    part = add_holes(
        part,
        [(-x, 0), (x, 0), (-90, 0), (90, 0)],
        M4_CLEARANCE,
    )

    return part


if __name__ == "__main__":
    export_part(make_part(), "WB105_LeftBeam")