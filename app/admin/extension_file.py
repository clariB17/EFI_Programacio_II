EXTENSIONS_LIB = set(['epub', 'pdf'])
EXTENSIONS_IMG = set(['png', 'jpeg', 'jpg'])

def libro_permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in EXTENSIONS_LIB

def imagen_permitida(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in EXTENSIONS_IMG