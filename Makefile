all: report.pdf

report.pdf: examples.tex
	xelatex -shell-escape report.tex
	xelatex -shell-escape report.tex

examples.tex:
	python3 build_examples.py

clean:
	rm -rf examples.tex report.pdf _minted-report __pycache__ *.aux *.log