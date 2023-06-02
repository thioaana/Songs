install :
		# Install dependencies
		pip install pip --upgrade pip \
		pip -r requirements.txt

format: 
		# Format Code
		black *.py blango/*.py blog/*.py blog/templatetags/*.py

lint:
		pylint --disable=R,C --generated-members=objects *.py blango/*.py blog/*.py blog/templatetags/*.py

all :	install format lint