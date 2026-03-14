with open('/home/jxlig0d/Escritorio/RRHH/RecursosHumanosCaixaBank/capitulos/cap3_tema3.tex', 'r') as f:
    lines = f.readlines()

del lines[553:]
del lines[446:471]
lines[443] = "\\section{Alternativas a la reducción de plantilla}\n"
del lines[426:440]
del lines[370:375]
del lines[305:313]
del lines[243:269]
del lines[198:209]
del lines[121:158]
lines[115] = "\\subsection{Criterios e indicadores para evaluar la planificación de RRHH}\n\nLa eficacia de la planificación de RRHH se mide a través de indicadores clave (KPIs) que permiten detectar desviaciones y tomar decisiones correctoras, aunque durante la entrevista no se recogieron datos específicos acerca de los indicadores que utiliza la organización.\n\n"
del lines[116:121]
del lines[91:115]
lines[12] = "%    3.6  Alternativas a la reducción de plantilla\n"

with open('/home/jxlig0d/Escritorio/RRHH/RecursosHumanosCaixaBank/capitulos/cap3_tema3.tex', 'w') as f:
    f.writelines(lines)
