"""
“Imagine you are in an office building with a bunch of identical elevator cars, 
and they all go to the same set of floors. 
You press the “up” or “down” button on your floor, and an elevator arrives promptly. 
Inside, you select your desired floor from a panel of buttons, and the elevator takes you there. 
Behind the scenes, the system efficiently manages elevator assignments and ignores requests in the wrong direction. 
Now, let’s design an elevator system that handles all of this.”




questions
multiple items?
change management | for example the remaning change for the customers is 5 and vending has a minimum note of 10

Requirements
Based on the conversation and how elevator systems work in the real world, here are the key functional requirements we’ve identified.

The system manages multiple elevator cars, all of which serve the same set of floors.
On each floor, there are “up” and “down” buttons that users press to call an elevator car before getting in.
Each elevator car should display its current floor and state (e.g., moving up, down, or idle).
Each elevator car has an internal control panel that includes buttons for every floor. Users inside the car press the button corresponding to the floor they want to go to.
If a user inside the elevator car presses a floor button in a direction opposite to the elevator's current movement, the request should be ignored.
Below are the non-functional requirements:

The dispatching algorithm should be configurable, allowing the system to easily switch between different optimization strategies.
Some of the requirements above are based on common sense in elevator systems. It’s a good idea to list them briefly during an interview to ensure everyone is on the same page. This way, the interviewer can step in if they want to adjust or clarify any assumptions. It helps save time and keeps the conversation aligned with the interviewer’s expectations.
"""


"""
passenger
requestElevator -> assignElevator (chosen based on strategy) -> Dispatches that elevator -> 
selectFloor -> save the selected floors -> ignore the ones in opposite direction -> move in the right direction -> stop at the selected floor
report elevator status
"""

from .elevator_status import (ElevatorStatus, DIRECTION)
from .dispatch_strategy import (DispatchStrategy) 
from .elevator_dispatch import (ElevatorDispatch)
from .elevator_system import ElevatorSystem
from .elevator_car import ElevatorCar 







