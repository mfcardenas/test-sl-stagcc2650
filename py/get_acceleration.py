#
# TI SimpleLink SensorTag 2016
# Date: 2016 10 17
#
# Sensor: Gyro, Accelerometer and Magnetometer
# Values: 9 bytes x, y, z for each sensor
# Note: Sensor values have not been validated
#
import struct
import sys
import traceback
import logging

from bluepy.btle import UUID, Peripheral, BTLEException

logging.basicConfig(level=logging.INFO, format='%(levelname)-6s %(asctime)-18s %(message)s', datefmt='%d-%m-%Y %H:%M:%S')

def TI_UUID(val):
    return UUID("%08X-0451-4000-b000-000000000000" % (0xF0000000 + val))


config_uuid = TI_UUID(0xAA82)
data_uuid = TI_UUID(0xAA81)

# Bit settings to turn on individual movement sensors
# bits 0 - 2: Gyro x, y z
# bits 3 - 5: Accelerometer x, y, z
# bit: 6: Magnetometer turns on X, y , z with one bit

# gyroOn = 0x0700
# accOn = 0x3800
# magOn = 0xC001

# sensorOnVal = gyroOn | magOn | accOn
sensorOnVal = 0x7F02

sensorOn = struct.pack("BB", (sensorOnVal >> 8) & 0xFF, sensorOnVal & 0xFF)
sensorOff = struct.pack("BB", 0x00, 0x00)

if len(sys.argv) != 2:
    logging.error("Fatal, must pass device address: %s %s", sys.argv[0], "<device address>")
    # print "Fatal, must pass device address: ", sys.argv[0], "<device address>"
    quit()

try:
    logging.info("Trying to connect to: %s", sys.argv[1])
    # print "Info, trying to connect to:", sys.argv[1]
    p = Peripheral(sys.argv[1])

except BTLEException:
    logging.error("Unable to connect!")
    # print "Fatal, unable to connect!"

except:
    logging.error("Unexpected error!")
    # print "Fatal, unexpected error!"
    traceback.print_exc()
    raise

else:

    try:
        # print "Info, connected and turning sensor on!"
        logging.info("Connected and turning sensor ON!")
        ch = p.getCharacteristics(uuid=config_uuid)[0]
        ch.write(sensorOn, withResponse=True)

        # print "Info, reading values!"
        logging.info("Reading values")
        ch = p.getCharacteristics(uuid=data_uuid)[0]
        for i in range(0, 50000):
            rawVals = ch.read()
            print "Raw:",
            for rawVal in rawVals:
                temp = ord(rawVal)
                print "%2.2x" % temp,
            print

            # Movement data: 9 bytes made up of x, y and z for Gyro, Accelerometer,
            # and Magnetometer.  Raw values must be divided by scale
            (gyroX, gyroY, gyroZ, accX, accY, accZ, magX, magY, magZ) = struct.unpack('<hhhhhhhhh', rawVals)

            scale = 128.0
            print "Gyro - x: %2.6f, y: %2.6f, z: %2.6f" % (gyroX / scale, gyroY / scale, gyroZ / scale)

            scale = 4096.0
            print "Acc - x: %2.6f, y: %2.6f, z: %2.6f" % (accX / scale, accY / scale, accZ / scale)

            scale = (32768.0 / 4912.0)
            print "Mag - x: %2.6f, y: %2.6f, z: %2.6f" % (magX / scale, magY / scale, magZ / scale)

        # print "Info, turning sensor off!"
        logging.info("Turning sensor OFF")
        ch = p.getCharacteristics(uuid=config_uuid)[0]
        ch.write(sensorOff, withResponse=True)

    except:
        # print "Fatal, unexpected error!"
        logging.error("Unexpected error!")
        traceback.print_exc()
        raise

    finally:
        # print "Info, disconnecting!"
        logging.info("Disconnecting...")
        p.disconnect()

finally:
    quit()
