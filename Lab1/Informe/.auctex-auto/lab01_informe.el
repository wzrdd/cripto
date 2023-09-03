(TeX-add-style-hook
 "lab01_informe"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "letter" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("geometry" "paperheight=27.94cm" "paperwidth=21.59cm" "bindingoffset=0in" "left=3cm" "right=2.0cm" "top=3.5cm" "bottom=2.5cm" "headheight=200pt" "headsep=1.0\\baselineskip") ("babel" "spanish" "es-tabla") ("inputenc" "utf8")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "geometry"
    "graphicx"
    "lastpage"
    "upgreek"
    "censor"
    "babel"
    "pdfpages"
    "tabularx"
    "adjustbox"
    "xcolor"
    "colortbl"
    "rotating"
    "multirow"
    "inputenc"
    "float"
    "fancyhdr"
    "hyperref"
    "listing"
    "lstautogobble")
   (TeX-add-symbols
    "PythonCode")
   (LaTeX-add-labels
    "fig:a1"
    "fig:a2-1"
    "fig:a2-2"
    "fig:a3")
   (LaTeX-add-environments
    "itquote")
   (LaTeX-add-xcolor-definecolors
    "commentcolor"
    "keywordcolor"
    "stringcolor"))
 :latex)

