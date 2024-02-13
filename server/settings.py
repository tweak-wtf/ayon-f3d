from ayon_server.settings import (
    BaseSettingsModel,
    SettingsField,
    MultiplatformPathListModel,
)


class F3DSettings(BaseSettingsModel):
    """f3d addon settings."""

    enabled: bool = SettingsField(True)
    f3d_path: MultiplatformPathListModel = SettingsField(
        title="Executable Path",
        default_factory=MultiplatformPathListModel,
        scope=["studio"],
    )
    default_hdri: str = SettingsField(
        default_factory=str,
        title="Default HDRI to load"
    )

DEFAULT_VALUES = {
    "enabled": True,
    "f3d_path": {
        "windows": [
            "C:\\Program Files\\F3D\\bin\\f3d.exe",
        ],
        "linux": [],
        "darwin": [],
    },
    "default_hdri": "",
}
