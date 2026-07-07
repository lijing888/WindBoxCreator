import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "cadquery"))

from common.parameters import *
from common.exporter import export_part
from common.geometry import create_plate, add_holes


def make_part():
    part = create_plate(40, MACHINE_WIDTH, BASE_THICKNESS, FILLET_SMALL)

    y = MACHINE_WIDTH / 2 - 25
    part = add_holes(
        part,
        [(0, -y), (0, y), (0, -70), (0, 70)],
        M4_CLEARANCE,
    )

    return part


if __name__ == "__main__":
    export_part(make_part(), "WB107_FrontBeam")