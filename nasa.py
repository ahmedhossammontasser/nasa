# python 3.8
import math

def get_fuel(mass , gravity, mult_value, sub_value):
    '''
        recursive function that calucalte fuel_needed for launch or land based on equation with gravity and mass (spaceship weigh or fuel_weigh), mult_value and sub_value as parameters 
    	:param mass: int
    	       gravity: float
    	       mult_value: float
    	       sub_value: int
    	:return: int fuel need for lauch a spaceship
    '''
    fuel_needed = math.floor( (mass * gravity * mult_value) - sub_value) 
    if fuel_needed < 0:
        return 0
    else :
        return fuel_needed + get_fuel( fuel_needed , gravity, mult_value, sub_value)


def get_weight_of_fuel(spaceship_weight, journey_list) :
    '''
        function calucalte total fuel needed for journey of spaceship with spaceship_weight and journey_list as parameters 
    	:param spaceship_weight: int
    	       journey_list: list of tuple (launch gravity, landing gravity)
    	:return: int total fuel needed for journey of spaceship
    '''
    fuel_weight_needed = 0
    for j_index in range(len(journey_list), 0, -1):
        landing_fuel_needed = get_fuel( spaceship_weight+fuel_weight_needed, journey_list[j_index-1][1] , 0.033, 42) 
        fuel_weight_needed += landing_fuel_needed
        launch_fuel_needed = get_fuel( spaceship_weight+fuel_weight_needed, journey_list[j_index-1][0] , 0.042, 33) 
        fuel_weight_needed += launch_fuel_needed
    return fuel_weight_needed

print( "Weight of fuel needed for Apollo 11: ", get_weight_of_fuel( 28801, [(9.807, 1.62), (1.62, 9.807)]) ) # 51898
print( "Weight of fuel needed for Mission on Mars:", get_weight_of_fuel( 14606, [(9.807, 3.711), (3.711, 9.807)]) ) # 33388
print( "Weight of fuel needed for Passenger ship: Earth to Moon To MarsTo Earth:", get_weight_of_fuel( 75432 , [(9.807, 1.62), (1.62, 3.711), (3.711, 9.807)]) ) # 212161
