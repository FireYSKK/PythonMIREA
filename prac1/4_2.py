import math
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
    def circle(center=0.5, shift=0., radius=0.1):
        return radius - (x - (center + shift)) ** 2 - (y - (center + shift)) ** 2
    # 10 - насыщенность цвета (больше - ярче цвет)
    return 10 * circle(shift=0.02), 10 * circle(shift=-0.02), 0


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
