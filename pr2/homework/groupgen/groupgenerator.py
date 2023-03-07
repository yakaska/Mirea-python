def generate_groups():
    groups = {'ИВБО': [], 'ИКБО': [], 'ИМБО': [], 'ИНБО': []}
    for ivbo in range(1, 9):
        groups['ИВБО'].append(f'ИВБО-{ivbo:02d}-21')
    for ikbo in range(1, 34):
        groups['ИКБО'].append(f'ИКБО-{ikbo:02d}-21')
    for imbo in range(1, 3):
        groups['ИМБО'].append(f'ИМБО-{imbo:02d}-21')
    for inbo in range(1, 14):
        groups['ИНБО'].append(f'ИНБО-{inbo:02d}-21')
    return groups


def make_grid(per_row, lst):
    copy_l = lst[:]
    nums_in_row = 1
    for i in range(len(lst)):
        if nums_in_row % per_row == 0:
            copy_l[i] = copy_l[i] + "\n"
            nums_in_row = 1
        else:
            copy_l[i] = copy_l[i] + "\t"
            nums_in_row += 1
    return "".join(copy_l)


def print_groups(groups):
    for key in groups.keys():
        print()
        print(key)
        print()
        print(make_grid(10, groups[key]))


print_groups(generate_groups())
