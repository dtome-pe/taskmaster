
#simple make rules, first use "make server port=8000(or another number)" that will bind server to that port
#then make client specifying path to config file that set server url accordingly

server:
	python3 ./main.py $(port)

client:
	python3 ./taskmaster_client/main.py $(path)