import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


# Ваш код здесь:
def func(x, y):
    color = circle(x, y, 0.3)

    return color, color, 0


def circle(x, y, rad):
    tcx = 0.5 - x
    tcy = 0.5 - y
    dist = (tcx * tcx + tcy * tcy) ** 0.5
    return 1 - smoothstep(dist, rad - (rad * 0.01), rad + (rad * 0.01))


def clamp(x, min_val, max_val):
    return min(max(x, min_val), max_val)


def smoothstep(x, edge0, edge1):
    t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
