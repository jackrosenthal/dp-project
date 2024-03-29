all: report.pdf

report.pdf: examples.tex report.tex dp.py
	pdflatex -shell-escape report.tex
	pdflatex -shell-escape report.tex

examples.tex: build_examples.py
	python3 build_examples.py

clean:
	rm -rf examples.tex report.pdf _minted-report __pycache__ *.aux *.log
