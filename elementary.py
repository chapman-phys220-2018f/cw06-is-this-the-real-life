#usr/bin/env python3
# -*- coding: utf-8 -*-

###
#Name: Morgan Holve
#Student_ID: 2281337
#Email: holve100@mail.chapman.edu
#Course: MATH220 FALL 2018
#Assignment: CW5
###

from scipy import constants




class Particle(object):
    """This class saves variables and attributes than an undefined particle would typically have""" 
    def __init__(self, x, y, z):
        """Sets default, or initial values, for each of the attributes"""
        self.position = (x, y, z)
        self.mass = 1.0
        self.momentum = (0.0, 0.0, 0.0)

    def impulse(self, px, py, pz):
        """Calculates a change in momentum given an impulse"""
        momentum_2 = (self.momentum[0] + px, self.momentum[1] + py, self.momentum[2] + pz)
        self.momentum = momentum_2
    def move(self, dt):
        """Calculates the position at some time interval dt"""
        change = ((dt * self.momentum[0] / self.mass), (dt * self.momentum[1] / self.mass), (dt * self.momentum[2] / self.mass))
        position_2 = (self.position[0] + change[0], self.position[1] + change[1], self.position[2] + change[2])
        self.position = position_2
class ChargedParticle(Particle): 
    """Adds a charge attribute to inheirited attributes"""
    def __init__(self, x, y, z, c):
        self.charge = c

class Electron(ChargedParticle):
    """Creates a class for all particles that are electrons"""
    def __init__(self, x, y, z):
        """Sets values to match those of an electron"""
        ChargedParticle.__init__(self, x, y, z, -constants.e)
        self.mass = constants.m_e

class Proton(ChargedParticle):
    """Creates a class for all particles that are protons"""
    def __init__(self, x, y, z):
        """Sets attributes to match those of a proton"""
        ChargedParticle.__init__(self, x, y, z, constants.e)
        self.mass = constants.m_p
