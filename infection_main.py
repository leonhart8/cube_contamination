"""
Module which defines the main program.

Initiates a cube of size supplied by the user, and a virus.

The virus starts its infection by infecting a random elementary cube of size one in the cube, and then grows
exponentially by infecting other neighboring cubes.
"""
import cube
import virus
import argparse
import time

if __name__ == '__main__':

    print("""
    ▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒
    ▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒
    ▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒
    ▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌
    ▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    █████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    █████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """)
    print()
    print("TIME FOR THE INFECTION TO START")
    time.sleep(3)
    print()

    # Parse command line arguments
    desc = "Executable of the infection simulation. Follow the usage\
     to set a cube of given size and launch a simulation"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-s", "--size", type=int, help="Size of the cube to be infected")
    args = parser.parse_args()

    # Generate cube and virus
    cu = cube.Cube(args.size)
    vir = virus.Virus(cu)

    # Launch infection
    time_step = vir.get_time_step()
    infection_rate = cu.infection_rate()

    # Virus determines the next cubes to infect
    vir.find_next_to_contaminate()
    amount_of_cubes_to_infect = len(vir.get_next_contaminated())

    while amount_of_cubes_to_infect > 0:

        # Printing infection metrics
        print("Current time step", time_step)
        print("Current infection rate {:0.3f}".format(infection_rate))

        # Virus infects the cubes
        vir.infect()

        # Compute new infection metrics
        time_step = vir.get_time_step()
        infection_rate = cu.infection_rate()

        # Finding next cubes to infect
        vir.find_next_to_contaminate()
        amount_of_cubes_to_infect = len(vir.get_next_contaminated())

    print()
    print("THE VIRUS WON HUMANITY LOST")
    print()

    print("Final infection rate {:0.3f}".format(infection_rate))
    print("Infection complete ! Amount of time steps :", time_step)

