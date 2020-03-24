def get_gps(vehicle):
    return str(vehicle.location.global_frame) #gps

def get_battery(vehicle):
    return str(vehicle.battery) #battery

def get_home(vehicle):
    return str(vehicle.home_location) #home

def get_distance(vehicle):
    return str(vehicle.rangefinder) #rangefinder distance


##vehicle.location.global_frame
##vehicle.location.global_relative_frame
##vehicle.location.local_frame

##vehicle.attitude
##vehicle.velocity
##vehicle.gimbal
##vehicle.battery
##vehicle.rangefinder
##vehicle.ekf_ok
##vehicle.last_heartbeat
##vehicle.system_status
##vehicle.heading
##vehicle.is_armable
##vehicle.airspeed
##vehicle.groundspeed
##vehicle.armed
##vehicle.mode
