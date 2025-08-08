
#simple make rules, first use "make server port=8000(or another number)" that will bind server to that port
#then make client the same way, this time, the port will be the target of client requests

server:
	python3 ./main.py $(port)

client:
	python3 ./taskmaster_client/main.py $(port)