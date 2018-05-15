all: clean build run

clean:
	rm --force --recursive data
	rm --force --recursive bin

build: # compile to binary (if you use interpreter, then do not implement it)
	pip3 install -r requirements.txt

run: 
	python3 src/scraper.py
