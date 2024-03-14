from pathlib import Path

from ayon_core.modules import AYONAddon, IPluginPaths

from .version import __version__
from .constants import ADDON_NAME, F3D_ROOT


class F3DAddon(AYONAddon, IPluginPaths):
    """Addon adds f3d functionality via plugins."""

    name = ADDON_NAME
    version = __version__

    def get_plugin_paths(self):
        return {"load": self.get_load_plugin_paths()}

    def get_load_plugin_paths(self, host_name=None):
        return [f"{Path(F3D_ROOT) / 'plugins' / 'load'}"]
