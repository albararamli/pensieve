import sys
import os
import subprocess
import numpy as np

import time, subprocess
from time import sleep

RUN_SCRIPT = 'run_video.py'
RANDOM_SEED = 42
RUN_TIME = 210 #280  # sec
ABR_ALGO = [ 'RL','robustMPC']#[ 'RL','BB','FIXED','robustMPC', 'fastMPC', 'BOLA',  'FESTIVE','RB']
#  [ 'RL','BB','FIXED','robustMPC', 'fastMPC', 'BOLA',  'FESTIVE','RB']
REPEAT_TIME = 1


def main():

	np.random.seed(RANDOM_SEED)

	with open('./chrome_retry_log', 'wb') as log:
		log.write('chrome retry log\n')
		log.flush()

		for rt in xrange(REPEAT_TIME):
			np.random.shuffle(ABR_ALGO)
			for abr_algo in ABR_ALGO:

				while True:
					###################################
					current_path=os.getcwd()
					new_path="../../pantheon/"
					os.chdir(new_path)
					os.system("touch ./data/DONE.txt")
					time.sleep(6)
					ttt='"python third_party/indigo/env/proxy.py 9999 LINUX;exit;exec bash"'
					os.system("gnome-terminal -e 'sh -c "+ttt+"'")
					os.chdir(current_path)
					##################################
					script = 'python ' + RUN_SCRIPT + ' ' + \
							  abr_algo + ' ' + str(RUN_TIME) + ' ' + str(rt)
					print(script)
					proc = subprocess.Popen(script,
							  stdout=subprocess.PIPE, 
							  stderr=subprocess.PIPE, 
							  shell=True)

					(out, err) = proc.communicate()
					print(out)
					print(err)
					if out == 'done\n' or out == 'timeout\n' or out == 'HTTP Error 400: Bad Request\n' or out == 'Timeout\n':
						break
					else:
						log.write(abr_algo + '_' + str(rt) + '\n')
						log.write(out + '\n')
						log.flush()
				###################################
				current_path=os.getcwd()
				new_path="../../pantheon/"
				os.chdir(new_path)
				os.system("touch ./data/DONE.txt")
				time.sleep(6)
				os.chdir(current_path)
				##################################
					


if __name__ == '__main__':
	main()
