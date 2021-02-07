train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1


# Convert °F to °C
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp


# Convert °C to °F
def c_to_f(c_temp):
    f_temp = c_temp * 9 / 5 + 32
    return f_temp


# Calculate force based on mass and accel
def get_force(mass, acceleration):
    force = mass * acceleration
    return force


# Calculate energy based on mass
def get_energy(mass, c=3*10**8):
    energy = mass * c**2
    return energy


# Calculate work performed based on mass, accel, and distance
def get_work(mass, acceleration, distance):
    work = get_force(mass, acceleration) * distance
    return work


# noinspection SpellCheckingInspection
f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies {} Newtons of force.".format(train_force))

bomb_energy = get_energy(bomb_mass)
print(bomb_energy)

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does {} Joules of work over {} meters.".format(train_work, train_distance))
