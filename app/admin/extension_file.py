EXTENSIONS_LIB = set(['epub', 'pdf'])
EXTENSIONS_IMG = set(['png', 'jpeg', 'jpg'])

<<<<<<< HEAD
=======

>>>>>>> b1f31ff0ea1df9b933757b4cd221104148494228
def libro_permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in EXTENSIONS_LIB

def imagen_permitida(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in EXTENSIONS_IMG