import schedule
import requests
import time
import matplotlib.pyplot as plt
import numpy as np
import jdatetime

data = []
successful_requests = 0
total_requests = 0
today = jdatetime.date.today()
report_string = ''
URL = 'https://jsonplaceholder.typicode.com/todos/1'

def get_date_label():
	today = jdatetime.date.today()
	return '{}-{}-{}'.format(today.year, today.month, today.day)

current_date = get_date_label()

NUMBER_OF_REQUESTS_IN_EACH_COLUMN = 12

def current_time() :
	datetime = jdatetime.datetime.now()
	return '[{}/{}/{} {}:{}:{}]:'.format(
		format(datetime.year, '04d'),
		format(datetime.month, '02d'),
		format(datetime.day, '02d'),
		format(datetime.hour, '02d'),
		format(datetime.minute, '02d'),
		format(datetime.second, '02d'),
	)

# Functions setup
def api_call():
	global current_date
	global successful_requests
	global total_requests
	global URL
	print((current_time()), end='\t')
	total_requests += 1
	try:
		response = requests.get(URL)
		print('{}\t(R.T. : ~{}s)'.format(response.status_code, round(response.elapsed.total_seconds(), 3)))
		if response.status_code == 200: successful_requests += 1
	except:
		print('error')
		pass

def collect_data_each_hour():
	global successful_requests
	global data
	global total_requests
	global report_string

	print('-'*20)
	print('{}\ttotal: {}, successful: {}, failed: {}'.format(current_time(), total_requests, successful_requests, total_requests - successful_requests))
	print('-'*20)
	with open("{}-log.txt".format(current_date), "a") as file:
		file.writelines(
			'{}  total: {}  successful: {}  failed: {}\n'
			.format(current_time(), total_requests, successful_requests, total_requests - successful_requests)
		)
	data.append(successful_requests)
	successful_requests = 0
	total_requests = 0

def plot():
	global successful_requests
	global current_date
	global data
	global report_string

	plt.rcParams["figure.figsize"] = (25, 10)
	plt.bar(
		np.arange(len(data))-0.125,
		data, width = 0.25, 
		color='g',
		label='success'
	)
	plt.bar(
		np.arange(len(data)) + 0.125,
		NUMBER_OF_REQUESTS_IN_EACH_COLUMN - np.array(data), width = 0.25,
		color='r',
		label='error'
	)
	plt.xticks(np.arange(len(data)))
	plt.title('Report ({})'.format(current_date))
	plt.ylabel('# REQUESTS (per Hour)')
	plt.xlabel('Time')

	plt.ylim([0, NUMBER_OF_REQUESTS_IN_EACH_COLUMN + 1])
	plt.savefig('{}-diagram.png'.format(current_date))

	data = []
	report_string = ''
	current_date = get_date_label()

# calling the api every 5 minutes
[[schedule.every().day.at("{}:{}".format(format(h, '02d'), format(m, '02d'))).do(api_call) for m in range(60)] for h in range(24)]


# collect data every hour
[schedule.every().day.at("{}:00".format(format(h, '02d'))).do(collect_data_each_hour) for h in range(24)]

schedule.every().day.at('00:00').do(plot)
if __name__ == "__main__":
	while True:
		schedule.run_pending()
		time.sleep(1)
