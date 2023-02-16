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
    body_x = 0.5 - x
    body_y = 0.5 - y
    dist_body = dist(body_x, body_y)

    eye_x = 0.55 - x
    eye_y = 0.32 - y
    dist_eye = dist(eye_x, eye_y)

    up_tr = body_y > 2 * body_x / 3 and x >= 0.5 and y >= 0.5
    lw_tr = body_y < -2 * body_x / 3 and x >= 0.5 >= y

    if x > 0.45 > y and 0.36 - dist_eye > 0.3:
        return 0, 0, 0
    elif up_tr or lw_tr:
        return 0, 0, 0
    elif 0.5 - dist_body > 0.2 and 0.5 - dist_body > 0.2:
        return 1, 1, 0
    else:
        return 0, 0, 0


def dist(pcx, pcy):
    return (pcx ** 2 + pcy ** 2) ** 0.5


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
