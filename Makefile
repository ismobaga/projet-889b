

.PHONY: rapport.pdf install run gen-data

rapport.pdf: rapport/projet.tex
	cd rapport && \
	pdflatex -interaction=nonstopmode projet.tex && \
	bibtex projet && \
	pdflatex -interaction=nonstopmode projet.tex && \
	pdflatex -interaction=nonstopmode projet.tex && \
	cp projet.pdf ../rapport.pdf

run: src/bench.py 
	python src/bench.py

runD: src/benchD.py install
	python src/benchD.py

gen-data: src/data.py install
	python src/data.py

install:
	pip install -Ur requirements.txt