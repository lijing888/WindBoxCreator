import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "cadquery"))

from common.exporter import export_part

from frame.WB101_Base_FL import make_part as make_wb101
from frame.WB102_Base_FR import make_part as make_wb102
from frame.WB103_Base_RL import make_part as make_wb103
from frame.WB104_Base_RR import make_part as make_wb104
from frame.WB105_LeftBeam import make_part as make_wb105
from frame.WB106_RightBeam import make_part as make_wb106
from frame.WB107_FrontBeam import make_part as make_wb107
from frame.WB108_RearBeam import make_part as make_wb108


parts = [
    ("WB101_Base_FL", make_wb101),
    ("WB102_Base_FR", make_wb102),
    ("WB103_Base_RL", make_wb103),
    ("WB104_Base_RR", make_wb104),
    ("WB105_LeftBeam", make_wb105),
    ("WB106_RightBeam", make_wb106),
    ("WB107_FrontBeam", make_wb107),
    ("WB108_RearBeam", make_wb108),
]


for name, maker in parts:
    export_part(maker(), name)

print("WB100 base plates exported.")