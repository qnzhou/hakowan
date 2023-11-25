from .render import render
from ..common import logger

import mitsuba as mi

if mi.variant() is None:
    for variant in ["cuda_ad_rgb", "llvm_ad_rgb", "scalar_rgb"]:
        if variant in mi.variants():
            mi.set_variant(variant)
            break
    assert mi.variant() is not None
