# README
This addon adds an action plugin to AYON Loader that loads the selected representation in f3d.
It's based on [ayon-djv](https://github.com/ynput/ayon-djv)
You can optionally specify a default hdri to use in the addons settings. Note that for now this only supports absolute paths.

It does not bundle or install f3d itself. Please specify the directory containing f3d binary in the addon settings.

## Supported files
For now this supports products of type `model` and their representations of type `["abc", "fbx", "usd"]`.

## Create package
To create addon package run `create_package.py` script in the root of repository.

```shell
python create_package.py
```

That will create `./package/`f3d`-<version>.zip` file which can be uploaded to AYON server.
