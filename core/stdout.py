#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys, ctypes

def set_cmd_text_color(color, handle=ctypes.windll.kernel32.GetStdHandle(-11)):
	Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
	return Bool


def resetColor():
	set_cmd_text_color(0x0f)
 

def printDarkGray(mess):
	set_cmd_text_color(0x08)
	sys.stdout.write(mess)
	resetColor()
 

def printDarkGreen(mess):
	set_cmd_text_color(0x02)
	sys.stdout.write(mess)
	resetColor()


def printDarkYellow(mess):
	set_cmd_text_color(0x06)
	sys.stdout.write(mess)
	resetColor()