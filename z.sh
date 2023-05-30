name="doc"
pdflatex $name.tex
pdflatex $name.tex # to get table of contents to show up
mv $name.pdf source.pdf
open source.pdf
mv $name.aux aux
mv $name.log aux
mv $name.toc aux
mv $name.out aux
