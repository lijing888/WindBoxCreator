import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "cadquery"))

from common.parameters import (
    BASE_TILE_LENGTH,
    BASE_TILE_WIDTH,
    BASE_THICKNESS,
    FILLET_SMALL,
    M4_CLEARANCE,
    MAGNET_DIAMETER,
    MAGNET_DEPTH,
)

from common.exporter import export_part
from common.geometry import (
    create_plate,
    add_holes,
    add_pockets,
    mirror_y,
)


def make_part():

    part = create_plate(
        BASE_TILE_LENGTH,
        BASE_TILE_WIDTH,
        BASE_THICKNESS,
        FILLET_SMALL,
    )

    x = BASE_TILE_LENGTH / 2 - 18
    y = BASE_TILE_WIDTH / 2 - 18

    part = add_holes(
        part,
        [
            (-x, -y),
            (x, -y),
            (-x, y),
            (x, y),
        ],
        M4_CLEARANCE,
    )

    part = add_pockets(
        part,
        [
            (-50, 0),
            (50, 0),
        ],
        MAGNET_DIAMETER,
        MAGNET_DEPTH,
    )

    # 镜像成为右前底板
    part = mirror_y(part)

    return part


if __name__ == "__main__":
    export_part(make_part(), "WB102_Base_FR")