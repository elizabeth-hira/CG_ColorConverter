import eel


eel.init("WEB")


@eel.expose
def rgb_to_xyz(r, g, b):
    try:
        var_r = (int(r) / 255.)
        var_g = (int(g) / 255.)
        var_b = (int(b) / 255.)
    except:
        return ["wrong params", "wrong params", "wrong params"]
    if 0 > var_r > 1 or 0 > var_g > 1 or 0 > var_b > 1:
        return ["wrong params", "wrong params", "wrong params"]

    if var_r > 0.04045:
        var_r = ((var_r + 0.055) / 1.055) ** 2.4
    else:
        var_r = var_r / 12.92
    if var_g > 0.04045:
        var_g = ((var_g + 0.055) / 1.055) ** 2.4
    else:
        var_g = var_g / 12.92
    if var_b > 0.04045:
        var_b = ((var_b + 0.055) / 1.055) ** 2.4
    else:
        var_b = var_b / 12.92

    var_r = var_r * 100
    var_g = var_g * 100
    var_b = var_b * 100

    X = var_r * 0.4124 + var_g * 0.3576 + var_b * 0.1805
    Y = var_r * 0.2126 + var_g * 0.7152 + var_b * 0.0722
    Z = var_r * 0.0193 + var_g * 0.1192 + var_b * 0.9505
    return [int(X + 0.5), int(Y + 0.5), int(Z + 0.5)]


@eel.expose
def rgb_to_hsv(r, g, b):
    try:
        var_r = (int(r) / 255.)
        var_g = (int(g) / 255.)
        var_b = (int(b) / 255.)
    except:
        return ["wrong params", "wrong params", "wrong params"]

    if 0 > var_r > 1 or 0 > var_g > 1 or 0 > var_b > 1:
        return ["wrong params", "wrong params", "wrong params"]

    var_Min = min(var_r, var_g, var_b)
    var_Max = max(var_r, var_g, var_b)
    del_Max = var_Max - var_Min

    V = var_Max

    if (del_Max == 0):
        H = 0
        S = 0
    else:

        S = del_Max / var_Max

        del_R = (((var_Max - var_r) / 6) + (del_Max / 2)) / del_Max
        del_G = (((var_Max - var_g) / 6) + (del_Max / 2)) / del_Max
        del_B = (((var_Max - var_b) / 6) + (del_Max / 2)) / del_Max

        if var_r == var_Max:
            H = del_B - del_G
        elif var_g == var_Max:
            H = (1 / 3) + del_R - del_B
        elif var_b == var_Max:
            H = (2 / 3) + del_G - del_R

        if H < 0:
            H += 1
        if H > 1:
            H -= 1
    return [int(H * 360), S, V]


@eel.expose
def xyz_to_rgb(x, y, z):
    try:
        var_X = (int(x) / 100.)
        var_Y = (int(y) / 100.)
        var_Z = (int(z) / 100.)
    except:
        return ["wrong params", "wrong params", "wrong params"]
    if 0 > var_X > 1 or 0 > var_Y > 1 or 0 > var_Z > 1:
        return ["wrong params", "wrong params", "wrong params"]

    var_r = var_X * 3.2406 + var_Y * -1.5372 + var_Z * -0.4986
    var_g = var_X * -0.9689 + var_Y * 1.8758 + var_Z * 0.0415
    var_b = var_X * 0.0557 + var_Y * -0.2040 + var_Z * 1.0570

    if var_r > 0.0031308:
        var_r = 1.055 * (var_r ** (1 / 2.4)) - 0.055
    else:
        var_r = 12.92 * var_r
    if var_g > 0.0031308:
        var_g = 1.055 * (var_g ** (1 / 2.4)) - 0.055
    else:
        var_g = 12.92 * var_g
    if var_b > 0.0031308:
        var_b = 1.055 * (var_b ** (1 / 2.4)) - 0.055
    else:
        var_b = 12.92 * var_b

    if var_r < 0:
        var_r = 0
    if var_g < 0:
        var_g = 0
    if var_b < 0:
        var_b = 0

    if var_r > 1:
        var_r = 1
    if var_g > 1:
        var_g = 1
    if var_b > 1:
        var_b = 1

    return [int(var_r * 255), int(var_g * 255), int(var_b * 255)]


@eel.expose
def xyz_to_hsv(x, y, z):
    rgb_arr = xyz_to_rgb(x, y, z)
    hsv_arr = rgb_to_hsv(rgb_arr[0], rgb_arr[1], rgb_arr[2])
    return [hsv_arr[0], hsv_arr[1], hsv_arr[2]]


@eel.expose
def hsv_to_rgb(h, s, v):
    try:
        var_h = (int(h) / 360.)
        var_s = float(s)
        var_v = float(v)
    except:
        return ["wrong params", "wrong params", "wrong params"]
    if 0 > var_h > 1 or 0 > var_s > 1 or 0 > var_v > 1:
        return ["wrong params", "wrong params", "wrong params"]

    if var_s == 0:
        var_r = var_v * 255
        var_g = var_v * 255
        var_b = var_v * 255
    else:
        h = var_h * 6
        if h == 6:
            h = 0
        var_i = int(h)
        var_1 = var_v * (1 - var_s)
        var_2 = var_v * (1 - var_s * (h - var_i))
        var_3 = var_v * (1 - var_s * (1 - (h - var_i)))

        if var_i == 0:
            var_r = var_v
            var_g = var_3
            var_b = var_1
        elif var_i == 1:
            var_r = var_2
            var_g = var_v
            var_b = var_1
        elif var_i == 2:
            var_r = var_1
            var_g = var_v
            var_b = var_3
        elif var_i == 3:
            var_r = var_1
            var_g = var_2
            var_b = var_v
        elif var_i == 4:
            var_r = var_3
            var_g = var_1
            var_b = var_v
        else:
            var_r = var_v
            var_g = var_1
            var_b = var_2

    return [int(var_r * 255), int(var_g * 255), int(var_b * 255)]


@eel.expose
def hsv_to_xyz(h, s, v):
    rgb_arr = hsv_to_rgb(h, s, v)
    xyz_arr = rgb_to_xyz(rgb_arr[0], rgb_arr[1], rgb_arr[2])
    return [xyz_arr[0], xyz_arr[1], xyz_arr[2]]

@eel.expose
def hex_to_palette(value):
    value = value.lstrip('#')
    rgb_arr = [int(value[i:i+2], 16) for i in (0, 2, 4)]
    xyz_arr = rgb_to_xyz(rgb_arr[0], rgb_arr[1], rgb_arr[2])
    hsv_arr = rgb_to_hsv(rgb_arr[0], rgb_arr[1], rgb_arr[2])
    return [rgb_arr, xyz_arr, hsv_arr]


eel.start("main.html")
