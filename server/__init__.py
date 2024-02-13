from typing import Type

from ayon_server.addons import BaseServerAddon, AddonLibrary

from .settings import F3DSettings, DEFAULT_VALUES
from .version import __version__


class FtrackAddon(BaseServerAddon):
    name = "f3d"
    title = "f3d"
    version = __version__
    settings_model: Type[F3DSettings] = F3DSettings

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)
