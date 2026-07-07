from pathlib import Path
from cadquery import exporters
from cadquery import Workplane


def export_part(part: Workplane, name: str) -> None:
    step_dir = Path("step")
    stl_dir = Path("stl")

    step_dir.mkdir(exist_ok=True)
    stl_dir.mkdir(exist_ok=True)

    exporters.export(part, str(step_dir / f"{name}.step"))
    exporters.export(part, str(stl_dir / f"{name}.stl"))

    print(f"Exported: {name}.step / {name}.stl")