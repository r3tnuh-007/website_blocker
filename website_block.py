import time as t
from datetime import datetime as dt

hosts_path = "/etc/hosts"
#hosts_path = "hosts"
redirect_ip = "127.0.0.1"

website_list = [
	"www.facebook.com",
	"www.youtube.com",
	"www.linkedin.com"
]

def block_websites():
	back = []
	start_hour = dt(dt.now().year, dt.now().month, dt.now().day, 0, 1)
	end_hour = dt(dt.now().year, dt.now().month, dt.now().day, 0, 50)
	i = 0
	y = 0
	while True:
		current_hour = dt(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, dt.now().minute)
		if  start_hour < current_hour < end_hour:
			file = open(hosts_path, 'a+')
			y = 0
			if i == 0:
				print("Working hour!")
				back.append(file.tell())
				for site in website_list:
					print(file.tell())
					file.write(redirect_ip + ' ' + site + "\n")

				i = 1
				file.close()
		else:
			i = 0
			if y == 0:
				file = open(hosts_path, 'a+')
				if (back != []):
					file.truncate(back[0])
				print("Fun hour!")
				file.close()
				y = 1
		t.sleep(1)

block_websites()
