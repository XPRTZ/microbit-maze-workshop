from microbit import i2c, sleep
import math


def twos_complement(val_lsb, val_msb):
    """
    This function converts bytes to int
    """
    raw = (val_msb << 8) | val_lsb
    if raw & 0x8000:
        raw = raw - 0x10000
    return raw


class Gyro():
    def __init__(self, addr=0x0D):
        self.addr = addr
        self.heading_offset = 0
        i2c.write(self.addr, bytearray([0x0B, 0x01]))  # Set/Reset period
        i2c.write(self.addr, bytearray([0x09, 0x1D]))  # Continuous mode, 200Hz, 8G, OSR=512

    def get_x_y_z(self):
        """
        Returns a tupel of 3 values, x, y, z
        """
        i2c.write(self.addr, b'\x00')
        data = i2c.read(self.addr, 6)
        x = twos_complement(data[0], data[1])
        y = twos_complement(data[2], data[3])
        z = twos_complement(data[4], data[5])
        return x, y, z

    def get_heading(self):
        """
        Returns the heading in float format, 0 - 360
        """
        x, y, z = self.get_x_y_z()
        heading = math.atan2(y, x) * (180 / math.pi)
        if heading < 0:
            heading += 360
        heading -= self.heading_offset
        if heading < 0:
            heading += 360
        return heading

    def get_heading_int(self):
        """
        Returns heading in int format 0 - 360
        """
        return int(self.get_heading())

    def reset_heading(self):
        """
        Resets the heading to 0
        """
        x, y, z = self.get_x_y_z()
        heading_offset = math.atan2(y, x) * (180 / math.pi)
        if heading_offset < 0:
            heading_offset += 360
        self.heading_offset = heading_offset

    def get_relative_heading(self):
        """
        Returns relative heading:
        0 = richting van offset
        positief = rechtsom (1 tot 179)
        negatief = linksom (-1 tot -179)
        """
        heading = self.get_heading()
        if heading > 180:
            return heading - 360  # linksom: wordt negatief
        else:
            return heading  # rechtsom: blijft positief