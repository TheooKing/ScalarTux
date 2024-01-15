from os import environ, path, getcwd
import json
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
# print(environ.get('PYGAME_HIDE_SUPPORT_PROMPT')) # debug

from .utils.colors import *
from .utils.settings import GlobalSettings, LocalSettings
# If there is a settings.json file in the same directory then 
#   try to import settings from there to the GlobalSettings class.
for file_name in ["settings.json", path.join(".","settings.json") ,path.join("tleng2","settings.json"), path.join(getcwd(), "tleng2","settings.json")]:
    try:
        with open(file_name) as settings_json:
            data = json.load(settings_json)
            print(data)

        break
    except:
        print(f"Could not find the settings.json file, moving on. (Tried {file_name})")
        print(path.exists(file_name))

from .utils.properties import GlobalProperties, LocalProperties
from .utils.debug import debug_print


from .engine.area import Area
from .engine.entity import Entity
from .engine.scene import Scene
from .engine.camera import Camera
from .engine.scene import Scene, SceneManager

from .ui_elements.label import Label
# from .ui_manager import 

from .physics.object import Object
from .physics.projectile import Projectile, Particles

from .services.animation import LazyAnimationService
from .services.image import ImageService
from .services.sound import SoundService
from .services.font import FontService
from .services.tilemap import TileMap, TileSet

from .utils.subpixel import SubPixelSurface


__all__ = [
'Area', 
'Entity', 
'Scene', 
'Camera', 
'Scene', 'SceneManager', 
'Label', 
'Object', 
'Projectile', 'Particles', 
'LazyAnimationService', 
'SoundService',
'ImageService', 
'FontService', 
'TileMap', 'TileSet', 
'GlobalSettings', 'LocalSettings',
'GlobalProperties', 'LocalProperties',
'debug_print',
'SubPixelSurface'
]


__author__ = "TheooKing/Theolaos"
__version__ = "v2.2.03-exp"

__name__ = "tleng2"
__doc__ = f'''TLeng2.py is a python 2d game engine

Current version is {__version__}

Current License:
MIT License

Copyright (c) 2023 Theofilos Nikolaos Savvidis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# Report:
# TODO: Settings Json support.
# TODO: Animation Json Support.
# TODO: Redo the Label system in update 2.2 and add:
#       capitilize / lower
#       striketrough, underlined
#       left|Center|Right
#       find
#       join
#       change_{smt}
#       __len__, __str__