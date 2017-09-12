import skywriter, os

last_tap = False
last_doubletap = False
last_flick = {"any":False, "north":False, "east":False, "south":False, "west":False}
last_move = ()
last_last_move = ()
move_detected = False
last_touch = {"any":False,"center":False,"north":False,"east":False,"south":False,"west":False}
kidfriendly = {"middle":"center","up":"north","right":"east","down":"south","left":"west"}


configFile = {"path":"tradfri.cfg","content":"[tradfri] \nhubip = 192.168.1.101\nsecurityid = C142ruJXimcqCcsb"}

if not os.path.exists(configFile["path"]):
    file = open(configFile["path"],"wb")
    file.write(configFile["content"]);
    file.close()


def kidspeak(s): #converting the kid language to skywriter arguments
    global kidfriendly
    if s in kidfriendly.keys():
        return kidfriendly[s]
    return s

@skywriter.tap()
def tap(location):
    global last_tap
    last_tap = True

@skywriter.double_tap()
def double_tap(position):
    global last_doubletap
    last_doubletap = True

@skywriter.flick()
def flick(start, end):
    global last_flick
    last_flick[end] = True
    last_flick["any"] = True

@skywriter.move()
def move(x,y,z):
    global last_move
    global last_last_move
    global move_detected
    last_last_move = last_move
    last_move = (x,y,z)
    move_detected = True

@skywriter.touch()
def touch(loc):
    global last_touch
    last_touch[loc] = True
    last_touch["any"] = True

def was_tapped():
    """
    Says whether or not the sensor was tapped.
    Returns True if sensor was tapped since this function was last called, False otherwise.
    """
    global last_tap
    if last_tap:
        last_tap = False
        return True
    return False

def was_double_tapped():
    """
    Says whether or not the sensor was double-tapped.
    Returns True if the sensor was double-tapped since this function was last called, False otherwise.
    """
    global last_doubletap
    if last_doubletap:
       last_doubletap = False
       return True
    return False

def was_flicked(where = "any"):
    """
    Says whether or not the sensor detected a flick. Can be used to check for a flick in a specific direction.
    Returns True if the sensor detected a flick which ended in the direction specified in the argument since the function was last called, False otherwise.
    """
    global last_flick
    where = kidspeak(where)
    if last_flick[where]:
        last_flick[where] = False
        last_flick["any"] = False
        return True
    return False

def was_touched(where = "any"):
    """
    Says whether or not the sensor was touched. Can be used to check for a touch in a specific part of the sensor.
    Returns True if the sesnor detected a touch in the location specified in the argument since this function was last called, False otherwise.
    """
    global last_touch
    where = kidspeak(where)
    if last_touch[where]:
        last_touch[where] = False
        last_touch["any"] = False
        return True
    return False

def get_pos():
    """
    Says where the sensor last detected something.
    Returns a tuple (x, y, z) of the location of the last action calling the skywriter.move() method.
    """
    global last_move
    return last_move

def was_moved():
    """
    Says whether the sensor has detected any movement since it was last checked.
    Returns True if the sensor detected movement since this function was last called, False otherwise.
    """
    global move_detected
    if move_detected:
        move_detected = False
        return True
    return False

def isOn():

   status = os.popen("python tradfri-status.py")
   with status as file:
      for line in file:
        if line[0] == 'b':
            if line[-2] == "f":
                return False
            elif line[-2] == "n":
                return True

def turnLightOn():
    """
    Turns light on
    """
    os.system("python2 tradfri-lights.py -l 65537 -a power -v on")

def turnLightOff():

    os.system("python2 tradfri-lights.py -l 65537 -a power -v off")

def setBrightness(brightness):
    os.system("python2 tradfri-lights.py -l 65537 -a brightness -v " + str(int(brightness * 100)))

def setColour(colourNumber):
    """
    Sets the colour of the light.

    :param colourNumber: Integer corresponding to the colour. 0:cold, 1:normal, 2:warm.
    """
    if colourNumber == 0:
        colour = "cold"
    elif colourNumber == 1:
        colour = "normal"
    elif colourNumber == 2:
        colour = "warm"
    else:
        print("That is not a colour")

    command = "python2 tradfri-lights.py -l 65537 -a color -v "+colour
    os.popen(command)


turnLightOn()