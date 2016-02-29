#!/usr/bin/python

from flask import Flask, jsonify, make_response, request
import conexion
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return "Proyecto de Redes"

@app.route('/datos')
def dat():
	return conexion.mostrar()

@app.route('/monitoreo',methods = ['GET'])
def monitoreo():
   	fecha = request.args.get('fecha', '')
	user = request.args.get('user', '')
	cpuus = request.args.get('cpuus', '')
	cpusy = request.args.get('cpusy', '')
	cpuid = request.args.get('cpuid', '')
	cpuwait = request.args.get('cpuwait', '')
	cpust = request.args.get('cpust', '')
	memswap = request.args.get('memswap', '')
	memfree = request.args.get('memfree', '')
	membuff = request.args.get('membuff', '')
	memcache = request.args.get('memcache', '')
	swapin = request.args.get('swapin', '')
	swapout = request.args.get('swapout', '')
	datos = "Fecha:"+fecha+" User:"+user+" CPUuser:"+cpuus+" CPUsystem:"+cpusy+" CPUidle:"+cpuid+" CPUwait:"+cpuwait+" CPUst:"+cpust+" MemSwap:"+memswap+" MemFree:"+memfree+" MemBuff:"+membuff+" MemCache:"+memcache+" SwapIn:"+swapin+" SwapOut:"+swapout+""
	conexion.guardar(datos)
        return "Hecho<P>"


if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0')

