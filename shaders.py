import glMath


def flat(render, **kwargs):
    # Normal calculada por poligono
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    intensity = glMath.Dot(triangleNormal, render.dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def gourad(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                      nA[1] * u + nB[1] * v + nC[1] * w,
                      nA[2] * u + nB[2] * v + nC[2] * w]

    intensity = glMath.Dot(triangleNormal, render.dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def toon(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                      nA[1] * u + nB[1] * v + nC[1] * w,
                      nA[2] * u + nB[2] * v + nC[2] * w]

    intensity = glMath.Dot(triangleNormal, render.dirLight)

    if intensity < 0.2:
        intensity = 0.1
    elif intensity < 0.5:
        intensity = 0.4
    elif intensity < 0.8:
        intensity = 0.7
    elif intensity <= 1:
        intensity = 1

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def glow(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                      nA[1] * u + nB[1] * v + nC[1] * w,
                      nA[2] * u + nB[2] * v + nC[2] * w]

    intensity = glMath.Dot(triangleNormal, render.dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    camForward = (render.camMatrix.item(0, 2),
                  render.camMatrix.item(1, 2),
                  render.camMatrix.item(2, 2))

    glowAmount = 1 - glMath.Dot(triangleNormal, camForward)

    if glowAmount <= 0:
        glowAmount = 0

    yellow = (1, 1, 0)

    b += yellow[2] * glowAmount
    g += yellow[1] * glowAmount
    r += yellow[0] * glowAmount

    if b > 1:
        b = 1
    if g > 1:
        g = 1
    if r > 1:
        r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def textureBlend(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                      nA[1] * u + nB[1] * v + nC[1] * w,
                      nA[2] * u + nB[2] * v + nC[2] * w]

    intensity = glMath.Dot(triangleNormal, render.dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if render.active_texture2:
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor2 = render.active_texture2.getColor(tU, tV)

        b += (1 - intensity) * texColor2[2]
        g += (1 - intensity) * texColor2[1]
        r += (1 - intensity) * texColor2[0]

    if b > 1:
        b = 1
    if g > 1:
        g = 1
    if r > 1:
        r = 1

    if b < 0:
        b = 0
    if g < 0:
        g = 0
    if r < 0:
        r = 0

    return r, g, b


def popshader(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                      nA[1] * u + nB[1] * v + nC[1] * w,
                      nA[2] * u + nB[2] * v + nC[2] * w]

    intensity = glMath.Dot(triangleNormal, render.dirLight)

    if intensity < 0.2:
        b = 0
        g = 1
        r = 0
    elif intensity < 0.5:
        b = 1
        g = 0
        r = 0
    elif intensity < 0.8:
        b = 0
        g = 0
        r = 1
    elif intensity <= 1:
        b = 0
        g = 1
        r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 1, 0, 1


def roseluminescent(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[0]
        g *= texColor[1]/3
        r *= texColor[2]

    return r, g, b


def orangeluminescent(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= 0
        g *= texColor[1]/2
        r *= texColor[2]

    return r, g, b


def blueluminescent(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= 1
        g *= 1
        r *= texColor[0]

    return r, g, b


def goldluminescent(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[0]
        g *= glMath.HEX(220)
        r *= glMath.HEX(220)

    return r, g, b


def Light(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                      nA[1] * u + nB[1] * v + nC[1] * w,
                      nA[2] * u + nB[2] * v + nC[2] * w]

    intensity = glMath.Dot(triangleNormal, render.dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def normalMap(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    tangent = kwargs["tangent"]
    bitangent = kwargs["bitangent"]

    b /= 255
    g /= 255
    r /= 255

    # P = Au + Bv + Cw
    tU = tA[0] * u + tB[0] * v + tC[0] * w
    tV = tA[1] * u + tB[1] * v + tC[1] * w

    if render.active_texture:
        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                      nA[1] * u + nB[1] * v + nC[1] * w,
                      nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = (-render.dirLight[0], -render.dirLight[1], -render.dirLight[2])

    if render.normal_map:
        texNormal = render.normal_map.getColor(tU, tV)
        texNormal = [texNormal[0] * 2 - 1,
                     texNormal[1] * 2 - 1,
                     texNormal[2] * 2 - 1]
        texNormal = glMath.Normalize(texNormal)

        tangentMatrix = [[tangent[0], bitangent[0], triangleNormal[0]],
                         [tangent[1], bitangent[1], triangleNormal[1]],
                         [tangent[2], bitangent[2], triangleNormal[2]]]

        texNormal = glMath.MV(tangentMatrix, texNormal)
        texNormal = glMath.Normalize(texNormal)

        intensity = glMath.Dot(texNormal, dirLight)
    else:
        intensity = glMath.Dot(triangleNormal, dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0
