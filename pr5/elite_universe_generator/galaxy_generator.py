import matplotlib.pyplot as plt
import matplotlib

seed = [0x5A4A, 0x0248, 0xB753]
pairs = '..LEXEGEZACEBISO' \
        'USESARMAINDIREA.' \
        'ERATENBERALAVETI' \
        'EDORQUANTEISRION'

x = list()
y = list()
n = list()


def tweak_seed():
    temp = sum(seed) % 0x10000
    seed[0] = seed[1]
    seed[1] = seed[2]
    seed[2] = temp
    return 2 * ((seed[1] >> 8) & 31)


def generate_system():
    longname_flag = seed[0] & 64
    name = list()
    x_coord = seed[1] >> 8
    y_coord = 255 - seed[0] >> 8

    pairs_num = [tweak_seed() for _ in range(4)]
    if not longname_flag:
        pairs_num.pop()
    for i in pairs_num:
        name.append(pairs[i])
        name.append(pairs[i + 1])

    name = ''.join([ch for ch in name if ch != '.'])
    return x_coord, y_coord, name


def main():
    matplotlib.style.use('dark_background')
    plt.figure(figsize=(24, 12))
    for i in range(256):
        tx, ty, tn = generate_system()
        x.append(tx)
        y.append(ty)
        n.append(tn)

    plt.scatter(x, y, s=2, color='white')
    for i, txt in enumerate(n):
        plt.annotate(txt, (x[i] + 0.5, y[i] + 0.5))

    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()
