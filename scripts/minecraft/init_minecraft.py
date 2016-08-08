#!/usr/bin/python3
# -*- coding: utf-8 -*-
# init_minecraft.py

import os
import sys

sys.path.append(os.path.join('..','..','worldbuild'))
import cls_interface_application as mod_if

mc = mod_if.InterfaceMineCraft('Minecraft server', 0.2)
mc.activate()
print(mc.send_command('/difficulty 2'))
print(mc.send_command('/op DynamiteBuilder'))
print(mc.send_command('/op craftandstore'))
print(mc.send_command('/give DynamiteBuilder minecraft:command_block'))
print(mc.send_command('/give craftandstore minecraft:command_block'))


