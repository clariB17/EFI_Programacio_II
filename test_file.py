from extension_file import libro_permitido, imagen_permitida
# __init__.py
def test_img_true():
    assert imagen_permitida('pepe.jpg') == True

def test_img_false():
    assert imagen_permitida('pepe.gif') == False

def test_lib_true():
    assert libro_permitido('pepe.pdf') == True

def test_lib_false():
    assert libro_permitido('pepe.docx') == False
    