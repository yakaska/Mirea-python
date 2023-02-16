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
    tcx = 0.5 - x
    tcy = 0.5 - y
    pct1 = dist(tcx, tcy)
    tcx = 0.42 - x
    tcy = 0.42 - y
    pct2 = dist(tcx, tcy)
    color1 = clamp((0.4 - pct1) * 2, 0.0, 1.0)
    color2 = clamp((0.4 - pct2) * 2, 0.0, 1.0)
    return color1, color2, 0


def dist(tcx, tcy):
    return (tcx * tcx + tcy * tcy) ** 0.5


def clamp(x, min_val, max_val):
    return min(max(x, min_val), max_val)


def lerp(a, b, x):
    return (1 - x) * a + x * b


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
