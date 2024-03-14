import time
from pathlib import Path

import ayon_api

from ayon_core.lib import run_detached_process
from ayon_core.pipeline import load

from ayon_f3d.utils import F3DExecutableCache
from ayon_f3d.constants import ADDON_NAME, F3D_ROOT
from ayon_f3d.version import __version__


class OpenInF3D(load.LoaderPlugin):
    """Open 3d asset with system default"""

    _executable_cache = F3DExecutableCache()
    addon_settings = ayon_api.get_addon_settings(ADDON_NAME, __version__)
    families = ["model"]
    representations = ["abc", "fbx", "usd"]
    extensions = ["*"]

    label = "Open in f3d"
    order = -10
    icon = "play-circle"
    color = "orange"

    @classmethod
    def get_f3d_path(cls):
        return cls._executable_cache.get_path()

    @classmethod
    def is_compatible_loader(cls, context):
        if not cls.get_f3d_path():
            return False
        return super().is_compatible_loader(context)

    def load(self, context, *args):
        path_to_open = Path(self.filepath_from_context(context))

        self.log.info("Opening : {}".format(path_to_open))

        # get basic f3d command parameters
        executable = self.get_f3d_path()
        f3d_config = Path(F3D_ROOT) / "config.json"
        if not all([executable, f3d_config]):
            raise AttributeError("invalid f3d settings")
        cmd = [
            executable,
            "--verbose=info",
            f"--config={f3d_config}",
        ]

        # get default hdri and append to command
        if self.addon_settings.get("default_hdri"):
            hdri_path = Path(self.addon_settings["default_hdri"])
            if not hdri_path.exists():
                raise FileNotFoundError(f'HDRI "{hdri_path}" was not found.')
            cmd.append(f"--hdri-file={hdri_path}")
            cmd.append("--hdri-ambient")
            cmd.append("--hdri-skybox")
            cmd.append("--blur-background")

        # lastly append file to open to command
        if not path_to_open.exists():
            raise FileNotFoundError(f'File "{path_to_open}" was not found.')
        cmd.append(f"{path_to_open}")

        # Run f3d with these commands
        self.log.info("Running f3d with command: {}".format(cmd))
        cmd = [str(c) for c in cmd] # ensure strings
        run_detached_process(cmd)
        # Keep process in memory for some time
        time.sleep(0.1)
