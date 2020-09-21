import sys

# ---------------------------------------------------------------------
# A script to hold Vesna in reset state and vice-versa 
# --> Because Vesna stays in the formed network even when application
# on LGTC is allready over. That may interfeer with other measurements.
# ---------------------------------------------------------------------

# Export GPIO2_2 or linuxPin-66 to user space 
try:
    os.system('echo 66 > /sys/class/gpio/export')
except:
    print("Pin already exported")

# Set the direction of the pin to output
os.system('echo out > /sys/class/gpio/gpio66/direction')

# Put Vesna into reset state, so it doesn't interfeer with other devices/measurements
if (int(sys.argv[1]) == 0):
    # Set the value to 0 - reset Vesna
    os.system('echo 0 > /sys/class/gpio/gpio66/value')
else:
    # Set value back to 1 - wake Vesna up
    os.system('echo 1 > /sys/class/gpio/gpio66/value')