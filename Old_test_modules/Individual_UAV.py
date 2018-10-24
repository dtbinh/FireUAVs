"""
DroneKit_simulator
Author: Joshua Shaffer (based on mission_basic.py example from DroneKit
Purpose: Test computer-based mission run of the fireUAV simulator in "real-time".
    Meant to figure out proper structure of running the simulator from a central
    node (i.e. the computer) and send proper commands to UAVs. Also aim to
    eventually test agency in UAVs (ability for them to override commands sent by
    the computer's simulation, but not commands sent by mission planner
"""

from __future__ import print_function

from dronekit import connect, VehicleMode, LocationGlobal
import time
import math
import pygame
from FireUAV_modules import Sim_Object

# Visualization parameters
WIDTH = 40
HEIGHT = 40
MARGIN_HALF = 2
sim_object = Sim_Object()


#Set up option parsing to get connection string
import argparse
parser = argparse.ArgumentParser(description='Demonstrates basic mission operations.')
parser.add_argument('--connect',
                   help="vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None

time.sleep(40)
#Start SITL if no connection string specified
if not connection_string:
    #sitl = dronekit_sitl.start_default()
    connection_strings = list()
    vehicle = list()
    origin = list()
    for i in range(0, sim_object.params.N):
        connection_strings.append('127.0.0.1:145' + str(50 + (i)*10))
        print('Connecting to vehicle on: %s' % connection_strings[i])
        vehicle.append(connect(connection_strings[i], wait_ready=True, baud=115200))
        origin.append(vehicle[i].location.global_frame)
        print(origin[i])

    input('wait...')

def get_location_metres(original_location, dNorth, dEast):
    """
    Returns a LocationGlobal object containing the latitude/longitude `dNorth` and `dEast` metres from the
    specified `original_location`. The returned Location has the same `alt` value
    as `original_location`.

    The function is useful when you want to move the vehicle around specifying locations relative to
    the current vehicle position.
    The algorithm is relatively accurate over small distances (10m within 1km) except close to the poles.
    For more information see:
    http://gis.stackexchange.com/questions/2951/algorithm-for-offsetting-a-latitude-longitude-by-some-amount-of-meters
    """
    earth_radius = 6378137.0  # Radius of "spherical" earth
    # Coordinate offsets in radians
    dLat = dNorth / earth_radius
    dLon = dEast / (earth_radius * math.cos(math.pi * original_location.lat / 180))

    # New position in decimal degrees
    newlat = original_location.lat + (dLat * 180 / math.pi)
    newlon = original_location.lon + (dLon * 180 / math.pi)
    return LocationGlobal(newlat, newlon, original_location.alt)


def get_distance_metres(aLocation1, aLocation2):
    """
    Returns the ground distance in metres between two LocationGlobal objects.

    This method is an approximation, and will not be accurate over large distances and close to the
    earth's poles. It comes from the ArduPilot test code:
    https://github.com/diydrones/ardupilot/blob/master/Tools/autotest/common.py
    """
    dlat = aLocation2.lat - aLocation1.lat
    dlong = aLocation2.lon - aLocation1.lon
    return math.sqrt((dlat * dlat) + (dlong * dlong)) * 1.113195e5

def get_distance_metres_xy(aLocation1, aLocation2, scale):
    """
    Returns the ground distance in metres between two LocationGlobal objects.

    This method is an approximation, and will not be accurate over large distances and close to the
    earth's poles. It comes from the ArduPilot test code:
    https://github.com/diydrones/ardupilot/blob/master/Tools/autotest/common.py
    """
    dlat = aLocation2.lat - aLocation1.lat
    dlong = aLocation2.lon - aLocation1.lon
    return dlong * 1.113195e5 / scale, dlat * 1.113195e5 / scale

'''def distance_to_current_waypoint():
    """
    Gets distance in metres to the current waypoint.
    It returns None for the first waypoint (Home location).
    """
    nextwaypoint = vehicle.commands.next
    if nextwaypoint == 0:
        return None
    missionitem = vehicle.commands[nextwaypoint - 1]  # commands are zero indexed
    lat = missionitem.x
    lon = missionitem.y
    alt = missionitem.z
    targetWaypointLocation = LocationGlobalRelative(lat, lon, alt)
    distancetopoint = get_distance_metres(vehicle.location.global_frame, targetWaypointLocation)
    return distancetopoint'''


'''def download_mission():
    """
    Download the current mission from the vehicle.
    """
    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()  # wait until download is complete.
    print(cmds)'''


def goto(dChange, tol_meter, scale):

    check_statement = False
    targetLocation = list()
    for i, idx in enumerate(dChange):
        currentLocation=vehicle[i].location.global_frame
        print(idx)
        targetLocation.append(get_location_metres(currentLocation, idx[1], idx[0]))
        print(targetLocation[i])
        print(vehicle[i])
        #input('wait...')
        vehicle[i].simple_goto(targetLocation[i], groundspeed=3.0)
        check_statement = check_statement or vehicle[i].mode.name=="GUIDED"

    while check_statement: #Stop action if we are no longer in guided mode.
        if update_visualizations(scale) is False:
            return False;

        remainingDistance = list()
        for i, quad in enumerate(vehicle):
            print(quad.location.global_frame)
            remainingDistance.append(get_distance_metres(
                quad.location.global_frame, targetLocation[i]))
            print('Vehicle ' + str(i) + ' remaining distance: ' + str(remainingDistance[i]))
        #remainingDistance=get_distance_metres(vehicle.location.global_frame, targetLocation)
        #print("Distance to target: ", remainingDistance)
        if all(dist<=tol_meter for dist in remainingDistance): #Just below target, in case of undershoot.
            print("All vehicles reached their targets")
            return True;
        #time.sleep(2)
        check_statement = False
        for quad in vehicle:
            check_statement = check_statement or quad.mode.name == "GUIDED"



def send_vehicle(locs, scale, tol_meter):
    #print(loc)
    loc_rel = list()
    change_rel = list()
    for i, idx in enumerate(locs):
        loc_rel.append(get_distance_metres_xy(origin[0], vehicle[i].location.global_frame, scale))
        change_rel.append(((idx[0] - (loc_rel[i][0] + 1.0)) * scale,
                           (idx[1] - (loc_rel[i][1] + 1.0)) * scale))

    return goto(change_rel, tol_meter, scale)


'''def update_vehicle_mission(aLocation, loc, scale):
    """
    Adds a takeoff command and four waypoint commands to the current mission.
    The waypoints are positioned to form a square of side length 2*aSize around the specified LocationGlobal (aLocation).

    The function assumes vehicle.commands matches the vehicle mission state
    (you must have called download at least once in the session and after clearing the mission)
    """

    # Get the set of commands from the vehicle
    cmds = vehicle.commands
    print(cmds)
    cmds.download()
    cmds.wait_ready()

    # Save the vehicle commands to a list
    missionlist = []
    for cmd in cmds:
        missionlist.append(cmd)

    print(" Clear any existing commands")
    cmds.clear()

    print("Adding new waypoint")
    # Add new commands. The meaning/order of the parameters is documented in the Command class.

    # Add MAV_CMD_NAV_TAKEOFF command. This is ignored if the vehicle is already in the air.
    #cmds.add(
    #    Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0,
    #            0, 0, 0, 0, 10))

    # Define the four MAV_CMD_NAV_WAYPOINT locations and add the commands
    point1 = get_location_metres(aLocation, loc[1] * scale, loc[0] * scale)
    #print(missionlist)
    #print(len(missionlist))

    if len(missionlist) > 1:
        cmds.add(missionlist[1])
    elif len(missionlist) == 1:
        cmds.add(missionlist[0])
    else:
        cmds.add(
            Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0,
                    0,
                    0, 0, 0, point1.lat, point1.lon, 10))
    #prev_count = prev_count + 1
    cmds.add(
        Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0,
                0, 0, 0, point1.lat, point1.lon, 10))

    print("Upload next waypoint to vehicle")
    #print(cmds)
    #input('wait...')
    cmds.upload()
    # TODO wait for confirmation'''


def arm_and_takeoff(aTargetAltitude, i):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't let the user try to arm until autopilot is ready
    while not vehicle[i].is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle[i].mode = VehicleMode("GUIDED")
    vehicle[i].armed = True

    while not vehicle[i].armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle[i].simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print(" Altitude: ", vehicle[i].location.global_relative_frame.alt)
        if vehicle[i].location.global_relative_frame.alt >= aTargetAltitude * 0.95:  # Trigger just below target alt.
            print("Reached target altitude")
            break
        time.sleep(1)


def close_all():
    print('Return to launch')
    for i, quad in enumerate(vehicle):
        quad.mode = VehicleMode("RTL")
        print("Close vehicle " + str(i+1) + " object")
        quad.close()
    # Shut down simulator if it was started.
    if sitl is not None:
        sitl.stop()


def update_visualizations(scale):
    params = sim_object.params
    env = sim_object.env
    fleet = sim_object.fleet

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    for row in range(params.height):
        for column in range(params.width):

            if env.cells[(column + 1, params.width - (row))].fire > 0:
                color = params.fire_color[env.cells[(column + 1, params.width - (row))].fire - 1]
            elif env.cells[(column + 1, params.width - (row))].obstacle == 1:
                color = params.obs_color
            else:
                color = params.fuel_color[env.cells[((column + 1), params.width - (row))].fuel]

            pygame.draw.rect(screen, color,
                             [(params.WIDTH) * column,
                              (params.HEIGHT) * (row), params.WIDTH,
                              params.HEIGHT])
            pygame.draw.rect(screen, (0, 0, 0),
                             [(params.WIDTH) * column,
                              (params.HEIGHT) * (row), params.WIDTH,
                              params.HEIGHT], params.MARGIN_HALF)

    for i in fleet.agents:
        # pygame.draw.circle(screen, (94, 154, 249), fleet.agents[i].display_loc(Params), 10)
        pygame.draw.polygon(screen, (94, 154, 249), fleet.agents[i].display_loc(params))
        #print(fleet.agents[i].display_loc(params))

    # TODO: add visuals for the real-life vehicle
    #print(vehicle.location.global_frame)
    for i, quad in enumerate(vehicle):
        x_loc, y_loc = get_distance_metres_xy(origin[0], quad.location.global_frame, scale)

        pygame.draw.circle(screen, (94, 154, 249),
                        [int(round(WIDTH * (x_loc) + WIDTH / 2)),
                            int(round(HEIGHT * (params.height- y_loc) - HEIGHT / 2))], 10)

    # Insert visualization update here
    # Limit to 60 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


def project_run():
    """
    Start up the simulation and arm vehicles to starting altitude
    """

    print('Priming FireUAV simulation')

    # From Copter 3.3 you will be able to take off using a mission item. Plane must take off using a mission item (currently).
    for i, quad in enumerate(vehicle):
        arm_and_takeoff(10, i)

    #vehicle.commands.next = 0
    #vehicle.mode = VehicleMode("AUTO")

    real_time_start = time.time()
    sim_time = 0.0
    sim_time_max_throttle = 3
    sim_time_min_throttle = 2
    sim_time_update = 1.0 # seconds
    sim_time_throttler = 0.1
    auto_run = True
    trigger = 0
    way_points_ahead = 1
    sim_update_number = 0
    way_point_number = 0

    #while True:
    #    ans = input('Ready to start?')
    #    if ans == 'No':
    #        close_all()
    #        return
    #    else:
    #        break

    while True:
        #listen()

        real_time = time.time() - real_time_start
        if auto_run is False:
            print('Not setup to run based on user input yet')
            close_all()
            break

        if update_visualizations(10.0) is False:
            close_all()
            break

        #real_time = time.time() - real_time_start
        #dif = sim_time - real_time
        #if dif < sim_time_min_throttle * sim_time_update and trigger == 1:
        #    close_all()
        #elif dif + sim_time_update > sim_time_max_throttle * sim_time_update:
        #    continue

        #if (dif > sim_time_min_throttle * sim_time_update and
        #        dif < sim_time_max_throttle * sim_time_update):
        #    trigger = 1
        #input('wait...')
        #nextwaypoint = vehicle.commands.next
        #print('Distance to waypoint (%s): %s' % (nextwaypoint, distance_to_current_waypoint()))
        #print(download_mission())
        #print(sim_update_number)
        #print(nextwaypoint)
        #if nextwaypoint == 1:
        #    continue  # TODO: add back in


        tar = divmod(sim_time, sim_time_update)
        if math.fabs(tar[1]) < 0.1 * sim_time_throttler or tar[1] == 0.0 or math.fabs(
                tar[1] - sim_time_update) < 0.1 * sim_time_throttler:
            locs = sim_object.synth_update(sim_time, sim_time_update)
            sim_update_number = sim_update_number + 1
            print(locs)
            #input('wait')
            #update_vehicle_mission(origin, locs, 10.0)
            if send_vehicle(locs, 10.0, 1.3) is False:
                close_all()
                break
            #vehicle.mode = VehicleMode("AUTO")
            print('Updated step')

        sim_object.update(sim_time_throttler)

        sim_time = sim_time + sim_time_throttler
        print(sim_time)

        #update()
        #transmit()



"""
script start
"""
pygame.init()
# Connect to the Vehicle
input('wait...')
'''close_all()
input('wait...')'''
window_size = [(WIDTH * sim_object.params.width),
               (HEIGHT * sim_object.params.height)]
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("UAVs on Fire")
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
project_run()


