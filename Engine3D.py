from pickle import GLOBAL
from gl import Renderer, color, V3, V2
import glMath as gm
from texture import Texture
from shaders import flat, normalMap, popshader, gourad, normalMap, toon, glow, roseluminescent, blueluminescent, goldluminescent

width = 1080
height = 720

rend = Renderer(width, height)

rend.dirLight = V3(0, 1, 0)


rend.background = Texture("models/oceanbg.bmp")
rend.glClearBackground()

modelPosition = V3(0.8, -1.5, -4)

#----------------------BALLENAS------------------------#
rend.active_texture = Texture("models/BallenaTexture.bmp")
rend.active_shader = gourad
rend.dirLight = V3(0, 1, 0)
rend.glLoadModel("models/ballena.obj",
                 translate=V3(-1.9, 1, -6.5),
                 scale=V3(0.7, 0.7, 0.7),
                 rotate=V3(0, -5, 30))
rend.glLoadModel("models/ballena.obj",
                 translate=V3(-0.4, 0.2, -6.5),
                 scale=V3(0.3, 0.3, 0.3),
                 rotate=V3(0, -5, 10))

#----------------------TIBURON------------------------#
rend.active_texture = Texture("models/SharkTexture.bmp")
rend.glLoadModel("models/tiburon.obj",
                 translate=V3(3, 3, -8),
                 scale=V3(0.5, 0.5, 0.5),
                 rotate=V3(10, 45, 0))

#----------------------PECES------------------------#
rend.active_shader = gourad
rend.active_texture = Texture("models/pez.bmp")
rend.glLoadModel("models/pez.obj",
                 translate=V3(4.2, 3.2, -8),
                 scale=V3(0.5, 0.5, 0.5),
                 rotate=V3(0, 45, 0))
rend.glLoadModel("models/pez.obj",
                 translate=V3(4.5, 3, -8),
                 scale=V3(0.5, 0.5, 0.5),
                 rotate=V3(0, 45, 0))
rend.glLoadModel("models/pez.obj",
                 translate=V3(4.45, 3.2, -8),
                 scale=V3(0.5, 0.5, 0.5),
                 rotate=V3(0, 45, 0))
rend.glLoadModel("models/pez.obj",
                 translate=V3(4.7, 3.35, -8),
                 scale=V3(0.5, 0.5, 0.5),
                 rotate=V3(0, 45, 0))
rend.glLoadModel("models/pez.obj",
                 translate=V3(4.5, 3.45, -8),
                 scale=V3(0.5, 0.5, 0.5),
                 rotate=V3(0, 45, 0))

#----------------------MANTARRAYA------------------------#
rend.dirLight = V3(0, 0, -1)
rend.active_shader = gourad
rend.active_texture = Texture("models/Fish_tex.bmp")
rend.glLoadModel("models/PezDorado.obj",
                 #  translate=V3(0.8, 0, -4),
                 translate=V3(0, -0.5, -1.8),
                 scale=V3(0.01, 0.01, 0.01),
                 rotate=V3(0, -160, 0))
rend.glLoadModel("models/PezDorado.obj",
                 #  translate=V3(0.8, 0, -4),
                 translate=V3(-0.6, -0.6, -2.2),
                 scale=V3(0.01, 0.01, 0.01),
                 rotate=V3(0, 160, -35))
rend.glLoadModel("models/PezDorado.obj",
                 #  translate=V3(0.8, 0, -4),
                 translate=V3(0.5, -0.5, -2.5),
                 scale=V3(0.01, 0.01, 0.01),
                 rotate=V3(0, -160, 0))

#----------------------DELFIN------------------------#
rend.active_shader = gourad
rend.active_texture = Texture("models/DelfnTexture.bmp")
rend.dirLight = V3(1, 0, 0)
rend.glLoadModel("models/delfin.obj",
                 translate=V3(0.90, -0.10, -1.9),
                 scale=V3(0.1, 0.1, 0.1),
                 rotate=V3(20, 5, 0))

#----------------------STONE------------------------#
# rend.active_shader = textureBlend

# rend.active_texture = Texture("models/norm.bmp")
# rend.dirLight = V3(1, 0, 0)
# rend.glLoadModel("models/Stone_O.obj",
#                  translate=V3(0.2, -0.5, -0.8),
#                  scale=V3(1, 1, 1),
#                  rotate=V3(0, 0, 0))

#----------------------FONDO MARINO------------------------#
rend.dirLight = V3(0.5, -0.5, 0)
rend.normal_map = Texture("models/SandStoneNormal.bmp")
rend.active_texture = Texture("models/SandStone.bmp")
rend.active_shader = normalMap
rend.glLoadModel("models/fondomarino.obj",
                 translate=V3(-4.5, -2.5, -4),
                 scale=V3(2, 1, 1),
                 rotate=V3(1, 0, 0))

#----------------------CORALES------------------------#
rend.active_texture = Texture("models/CoralTexture1.bmp")
rend.active_shader = roseluminescent
rend.dirLight = V3(1, 0, 0)
rend.glLoadModel("models/coral1.obj",
                 translate=V3(-1, -1, -1.5),
                 scale=V3(1.2, 1.2, 1.2),
                 rotate=V3(0, 0, 0))
rend.active_shader = blueluminescent
rend.active_texture = Texture("models/coral2Texture.bmp")
rend.glLoadModel("models/coral2.obj",
                 translate=V3(0.75, -1, -1.2),
                 scale=V3(1, 1, 1),
                 rotate=V3(0, 0, 0))
rend.active_shader = goldluminescent
rend.active_texture = Texture("models/coral2Texture.bmp")
rend.glLoadModel("models/coral3.obj",
                 translate=V3(0.40, -1, -1.2),
                 scale=V3(1, 1, 1),
                 rotate=V3(0, 0, 0))
rend.active_texture = Texture("models/coral2Texture.bmp")
rend.glLoadModel("models/coral3.obj",
                 translate=V3(-0.15, -1, -1.2),
                 scale=V3(1, 1, 1),
                 rotate=V3(0, 180, 0))
rend.active_texture = Texture("models/CoralTexture1.bmp")
rend.active_shader = roseluminescent
rend.dirLight = V3(1, 0, 0)
rend.glLoadModel("models/coral1.obj",
                 translate=V3(0.5, -1.5, -2),
                 scale=V3(1.2, 1.2, 1.2),
                 rotate=V3(0, 0, 0))
rend.active_shader = blueluminescent
rend.active_texture = Texture("models/coral2Texture.bmp")
rend.glLoadModel("models/coral2.obj",
                 translate=V3(-0.5, -1.2, -1.8),
                 scale=V3(1, 1, 1),
                 rotate=V3(0, 0, 0))

rend.glFinish("output.bmp")
