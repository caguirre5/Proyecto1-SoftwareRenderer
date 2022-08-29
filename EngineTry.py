from pickle import GLOBAL
from gl import Renderer, color, V3, V2
import glMath as gm
from texture import Texture
from shaders import flat, popshader, unlit, gourad, toon, glow, textureBlend

width = 1080
height = 720

rend = Renderer(width, height)

rend.dirLight = V3(0, -1, 0)


rend.glClearColor(gm.HEX(18), gm.HEX(87), gm.HEX(115))
rend.glClear()

modelPosition = V3(0.8, -1.5, -4)

#----------------------BALLENAS------------------------#
rend.active_texture = Texture("models/armor.bmp")
rend.active_shader = gourad
rend.dirLight = V3(1, 0, 0)
rend.glLoadModel("models/knight.obj",
                 translate=V3(2, -1.5, -1.2),
                 scale=V3(1, 1, 1),
                 rotate=V3(0, -150, 0))

#----------------------BALLENAS------------------------#
rend.active_texture = None
rend.active_shader = gourad
rend.glLoadModel("models/DragonEggFree.obj",
                 translate=V3(2, -1.5, -6),
                 scale=V3(1, 1, 1),
                 rotate=V3(0, -150, 0))

rend.glFinish("output2.bmp")
