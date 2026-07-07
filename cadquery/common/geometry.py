import cadquery as cq


def create_plate(length, width, thickness, fillet=2):
    """
    创建矩形底板
    """

    part = (
        cq.Workplane("XY")
        .box(length, width, thickness)
        .edges("|Z")
        .fillet(fillet)
    )

    return part


def add_holes(part, points, diameter):
    """
    添加通孔
    """

    return (
        part.faces(">Z")
        .workplane()
        .pushPoints(points)
        .hole(diameter)
    )


def add_pockets(part, points, diameter, depth):
    """
    添加磁铁孔
    """

    return (
        part.faces(">Z")
        .workplane()
        .pushPoints(points)
        .hole(diameter, depth)
    )


def add_rib(
    part,
    x,
    y,
    length,
    width,
    height,
):
    """
    添加加强筋
    """

    rib = (
        cq.Workplane("XY")
        .center(x, y)
        .box(length, width, height)
    )

    return part.union(rib)


def mirror_x(part):
    return part.mirror("YZ")


def mirror_y(part):
    return part.mirror("XZ")