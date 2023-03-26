from pr5.elite_universe_generator.Star import Star, rshift


def create_galaxy_seed(init_seed, roll):
    new_seed = []
    if roll == 0:
        return init_seed

    for j in range(roll):
        for i in range(4):
            right = init_seed[i]
            left = rshift(init_seed[i], 8)

            if (right & 0x80) == 0x80:
                right = right << 1
                right += 1
            else:
                right = right << 1

            if (left & 0x80) == 0x80:
                left = left << 1
                left += 1
            else:
                left = left << 1
            new_seed = (right & 0xFF) | (left << 8)
    return new_seed


def generate_galaxy(galaxy_number, planet_number):
    seed = [0x5A4A, 0x0248, 0xB753]
    star = Star()

    seed = create_galaxy_seed(seed, galaxy_number)

    star.init_star(seed)
    new_seed = star.seed

    for i in range(planet_number):
        new_seed = star.twist(new_seed)
        new_seed = star.twist(new_seed)
        new_seed = star.twist(new_seed)
        new_seed = star.twist(new_seed)
    star.init_star(new_seed)
    return star


def print_star(star):
    print(f'Name: {star.planet_name}')
    print(f'Loc: ({star.x};{star.y})')
    print(f'Radius: {star.radius}')
    print(f'Government: {star.gov_name}')
    print(f'Economy: {star.eco_name}')
    print(f'Inhabitants: {star.inhabitants}')
    print(f'Tech level: {star.tech_lvl}')
    print(f'Population: {star.pops} billion')
    print(f'Production: {star.prod}')


if __name__ == '__main__':
    while True:
        galaxy_number = int(input("Номер галактики"))
        planet_number = int(input("Номер планеты"))
        print_star(generate_galaxy(galaxy_number, planet_number))
