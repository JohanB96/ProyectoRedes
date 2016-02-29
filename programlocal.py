#!/usr/bin/python
from flask import Flask, jsonify, make_response
import subprocess


def who():
	who = subprocess.Popen(['who'], stdout = subprocess.PIPE)
	cut = subprocess.Popen(['cut', '-d', ' ', '-f', '1'], stdin = who.stdout, stdout = subprocess.PIPE)
	output = subprocess.check_output(('uniq'), stdin = cut.stdout)
	return output

def cpuwa(param):
	vmstat = subprocess.Popen(['vmstat'], stdout = subprocess.PIPE)
	tail = subprocess.Popen(['tail','-n','+3'], stdin = vmstat.stdout, stdout = subprocess.PIPE)
	tr = subprocess.Popen(['tr', '-s', ' '], stdin = tail.stdout, stdout = subprocess.PIPE)
	if (param == "us"):
		value = "14"
	elif (param == "sy"):
		value = "15"
	elif (param == "id"):
		value = "16"
	elif (param == "wa"):
		value = "17"
	elif (param == "st"):
		value = "18"
	output = subprocess.check_output(['cut', '-d', ' ', '-f', value], stdin = tr.stdout)
	return output

def mem(param):
	vmstat = subprocess.Popen(['vmstat'], stdout = subprocess.PIPE)
	tail = subprocess.Popen(['tail','-n','+3'], stdin = vmstat.stdout, stdout = subprocess.PIPE)
	tr = subprocess.Popen(['tr', '-s', ' '], stdin = tail.stdout, stdout = subprocess.PIPE)
	if (param == "swpd"):
		value = "4"
	elif (param == "free"):
		value = "5"
	elif (param == "buff"):
		value = "6"
	elif (param == "cache"):
		value = "7"
	output = subprocess.check_output(['cut', '-d', ' ', '-f', value], stdin = tr.stdout)
	return output

def swap(param):
	vmstat = subprocess.Popen(['vmstat'], stdout = subprocess.PIPE)
	tail = subprocess.Popen(['tail','-n','+3'], stdin = vmstat.stdout, stdout = subprocess.PIPE)
	tr = subprocess.Popen(['tr', '-s', ' '], stdin = tail.stdout, stdout = subprocess.PIPE)
	if (param == "si"):
		value = "8"
	elif (param == "so"):
		value = "9"

	output = subprocess.check_output(['cut', '-d', ' ', '-f', value], stdin = tr.stdout)
	return output

def creaciontxt(x):
    archi=open('/home/johan/Documentos/datos.txt','a')
    archi.write('Linea ' + x + '\n')
    archi.close()

def enviar():
	fecha = ""+subprocess.check_output(['date','+%H:%M-%d-%m-%y'])[:-1]
	user = ""+who()[:-1]
	cpuus = ""+cpuwa("us")[:-1]
	cpusy = ""+cpuwa("sy")[:-1]
	cpuid = ""+cpuwa("id")[:-1]
	cpuwait = ""+cpuwa("wa")[:-1]
	cpust = ""+cpuwa("st")[:-1]
	memswap = ""+mem("swpd")[:-1]
	memfree = ""+mem("free")[:-1]
	membuff = ""+mem("buff")[:-1]
	memcache = ""+mem("cache")[:-1]
	swapin = ""+swap("si")[:-1]
	swapout = ""+swap("so")[:-1]
	url = "http://proyectoredes-redesproyecto.rhcloud.com/monitoreo?fecha="+fecha+"&user="+user+"&cpuus="+cpuus+"&cpusy="+cpusy+"&cpuid="+cpuid+"&cpuwait="+cpuwait+"&cpust="+cpust+"&memswap="+memswap+"&memfree="+memfree+"&membuff="+membuff+"&memcache="+memcache+"&swapin="+swapin+"&swapout="+swapout+""
	creaciontxt(url)
	subprocess.call(['curl',url])

enviar()
