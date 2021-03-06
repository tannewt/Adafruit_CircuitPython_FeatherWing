# The MIT License (MIT)
#
# Copyright (c) 2017 Scott Shawcroft for Adafruit Industries LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_featherwing.motor_featherwing`
====================================================

Helper for using motors with the `Motor FeatherWing <https://www.adafruit.com/product/2927>`_.

* Author(s): Scott Shawcroft
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing.git"

from adafruit_motor import motor, stepper
from adafruit_pca9685 import PCA9685

from adafruit_featherwing import shared

class MotorFeatherWing:
    """Class representing an `Adafruit Motor FeatherWing <https://www.adafruit.com/product/2927>`_.

       Automatically uses the feather's I2C bus."""
    def __init__(self):
        self._motor1 = None
        self._motor2 = None
        self._motor3 = None
        self._motor4 = None
        self._stepper1 = None
        self._stepper2 = None
        self._pca = PCA9685(shared.I2C_BUS, address=0x60)
        self._pca.frequency = 1600

    @property
    def motor1(self):
        """:py:class:`~adafruit_motor.motor.DCMotor` controls for motor 1.

            .. image :: /_static/motor_featherwing/m1.jpg
              :alt: Motor 1 location

            This example moves the motor forwards for one fifth of a second at full speed.

            .. code-block:: python

                import time
                from adafruit_featherwing import motor_featherwing

                wing = motor_featherwing.MotorFeatherWing()

                wing.motor1.throttle = 1.0
                time.sleep(0.2)

                wing.motor1.throttle = 0
        """
        if not self._motor1:
            if self._stepper1:
                raise RuntimeError("Cannot use motor1 at the same time as stepper1.")
            self._pca.channels[8].duty_cycle = 0xffff
            self._motor1 = motor.DCMotor(self._pca.channels[9], self._pca.channels[10])
        return self._motor1

    @property
    def motor2(self):
        """:py:class:`~adafruit_motor.motor.DCMotor` controls for motor 2.

            .. image :: /_static/motor_featherwing/m2.jpg
              :alt: Motor 2 location

            This example moves the motor forwards for one fifth of a second at full speed.

            .. code-block:: python

                import time
                from adafruit_featherwing import motor_featherwing

                wing = motor_featherwing.MotorFeatherWing()

                wing.motor2.throttle = 1.0
                time.sleep(0.2)

                wing.motor2.throttle = 0
        """
        if not self._motor2:
            if self._stepper1:
                raise RuntimeError("Cannot use motor2 at the same time as stepper1.")
            self._pca.channels[13].duty_cycle = 0xffff
            self._motor2 = motor.DCMotor(self._pca.channels[11], self._pca.channels[12])
        return self._motor2

    @property
    def motor3(self):
        """:py:class:`~adafruit_motor.motor.DCMotor` controls for motor 3.

            .. image :: /_static/motor_featherwing/m3.jpg
              :alt: Motor 3 location

            This example moves the motor forwards for one fifth of a second at full speed.

            .. code-block:: python

                import time
                from adafruit_featherwing import motor_featherwing

                wing = motor_featherwing.MotorFeatherWing()

                wing.motor3.throttle = 1.0
                time.sleep(0.2)

                wing.motor3.throttle = 0
        """
        if not self._motor3:
            if self._stepper2:
                raise RuntimeError("Cannot use motor3 at the same time as stepper2.")
            self._pca.channels[2].duty_cycle = 0xffff
            self._motor3 = motor.DCMotor(self._pca.channels[3], self._pca.channels[4])
        return self._motor3

    @property
    def motor4(self):
        """:py:class:`~adafruit_motor.motor.DCMotor` controls for motor 4.

            .. image :: /_static/motor_featherwing/m4.jpg
              :alt: Motor 4 location

            This example moves the motor forwards for one fifth of a second at full speed.

            .. code-block:: python

                import time
                from adafruit_featherwing import motor_featherwing

                wing = motor_featherwing.MotorFeatherWing()

                wing.motor4.throttle = 1.0
                time.sleep(0.2)

                wing.motor4.throttle = 0
        """
        if not self._motor4:
            if self._stepper2:
                raise RuntimeError("Cannot use motor4 at the same time as stepper2.")
            self._pca.channels[7].duty_cycle = 0xffff
            self._motor4 = motor.DCMotor(self._pca.channels[5], self._pca.channels[6])
        return self._motor4

    @property
    def stepper1(self):
        """:py:class:`~adafruit_motor.stepper.StepperMotor` controls for one connected to stepper 1
           (also labeled motor 1 and motor 2).

            .. image :: /_static/motor_featherwing/stepper1.jpg
              :alt: Stepper 1 location

            This example moves the stepper motor 100 steps forwards.

            .. code-block:: python

                from adafruit_featherwing import motor_featherwing

                wing = motor_featherwing.MotorFeatherWing()

                for i in range(100):
                    wing.stepper1.onestep()"""
        if not self._stepper1:
            if self._motor1 or self._motor2:
                raise RuntimeError("Cannot use stepper1 at the same time as motor1 or motor2.")
            self._pca.channels[8].duty_cycle = 0xffff
            self._pca.channels[13].duty_cycle = 0xffff
            self._stepper1 = stepper.StepperMotor(self._pca.channels[10], self._pca.channels[9],
                                                  self._pca.channels[11], self._pca.channels[12])
        return self._stepper1

    @property
    def stepper2(self):
        """:py:class:`~adafruit_motor.stepper.StepperMotor` controls for one connected to stepper 2
           (also labeled motor 3 and motor 4).

            .. image :: /_static/motor_featherwing/stepper2.jpg
              :alt: Stepper 2 location

            This example moves the stepper motor 100 steps forwards.

            .. code-block:: python

                from adafruit_featherwing import motor_featherwing

                wing = motor_featherwing.MotorFeatherWing()

                for i in range(100):
                    wing.stepper2.onestep()
        """
        if not self._stepper2:
            if self._motor3 or self._motor4:
                raise RuntimeError("Cannot use stepper2 at the same time as motor3 or motor4.")
            self._pca.channels[7].duty_cycle = 0xffff
            self._pca.channels[2].duty_cycle = 0xffff
            self._stepper2 = stepper.StepperMotor(self._pca.channels[4], self._pca.channels[3],
                                                  self._pca.channels[5], self._pca.channels[6])
        return self._stepper2
