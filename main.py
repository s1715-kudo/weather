#!/usr/bin/env python
# -*- coding: utf-8 -*-
import weather
import csv
import datetime

def main():
	past=[]
	forecast=[]
	with open("setting.txt") as f:
		for l in [row for row in csv.reader(f)]:
			past.append(weather.AmeDAS(l[1],l[0]))
			forecast.append(weather.forecast(past[len(past)-1].all[1]))
		f.close()
		
	with open("logtime.txt",mode='w') as f:
		f.write(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

if __name__=='__main__':
	main()