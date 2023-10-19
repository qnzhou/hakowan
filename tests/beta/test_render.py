import pytest
import pathlib
import hakowan.beta as hkw
from hakowan.beta.render.render import generate_scene_config
import lagrange
import numpy as np

from .asset import triangle, two_triangles


class TestRender:
    def test_render(self, triangle):
        mesh = triangle
        base = hkw.layer.Layer().data(mesh).mark(hkw.mark.Surface)

        scene = hkw.compiler.compile(base)
        scene_config = generate_scene_config(scene)
        assert len(scene_config) == 1

        for shape_id, shape in scene_config.items():
            assert shape["type"] == "ply"
            assert pathlib.Path(shape["filename"]).exists()

    def test_point_cloud(self, triangle):
        mesh = triangle
        base = hkw.layer.Layer().data(mesh).mark(hkw.mark.Point)

        scene = hkw.compiler.compile(base)
        scene_config = generate_scene_config(scene)
        assert len(scene_config) == 3

        for shape_id, shape in scene_config.items():
            assert shape["type"] == "sphere"
            assert shape["radius"] > 0
            for key, value in shape.items():
                if key.startswith("bsdf"):
                    assert value["type"] == "diffuse"

    def test_point_cloud_with_size(self, triangle):
        mesh = triangle
        mesh.create_attribute(
            "size",
            element=lagrange.AttributeElement.Vertex,
            usage=lagrange.AttributeUsage.Scalar,
            initial_values=np.array([1, 2, 3], dtype=np.float32),
        )
        base = hkw.layer.Layer().data(mesh)
        l0 = base.mark(hkw.mark.Point).channel(size="size")
        l1 = base.mark(hkw.mark.Surface)
        scene = hkw.compiler.compile(l0 + l1)
        scene_config = generate_scene_config(scene)
