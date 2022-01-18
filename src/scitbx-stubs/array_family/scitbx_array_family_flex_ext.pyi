# In real code this is the root and .flex is the derivation.
#
# This seems.. somewhat excessive to reproduce in the type system, and
# most of the things you would want to read from this are just injected
# onto the actual class instance anyway.
from __future__ import annotations

from .flex import *
