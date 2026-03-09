# ============================================================
#  .latexmkrc — Configuración de latexmk para este proyecto
#  latexmk usará pdflatex y generará el PDF en la raíz del proyecto.
# ============================================================

# Usar pdflatex (genera PDF directamente)
$pdf_mode = 1;
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';

# Directorio de salida de archivos auxiliares
# (descomenta si quieres mantener la raíz limpia)
# $out_dir = 'compilado';

# Número máximo de pasadas
$max_repeat = 5;

# Extensiones a limpiar con latexmk -c
@generated_exts = (
    'aux', 'bbl', 'bcf', 'blg', 'fls', 'fdb_latexmk',
    'idx', 'ind', 'ilg', 'lof', 'lot', 'log',
    'nav', 'out', 'run.xml', 'snm', 'synctex.gz',
    'toc', 'vrb', 'xdv'
);
