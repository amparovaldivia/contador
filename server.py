from registro import app
from registro.controlers import controlador
app.secret_key="secreto"
if __name__=='__main__':
    app.run(debug=True)
