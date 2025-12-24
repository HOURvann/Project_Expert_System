from app import create_app

app = create_app()

if __name__ == '__main__':
    # ត្រូវតែមាន app.run(...) នៅទីនេះ ទើបវាដំណើរការ!
    app.run(debug=True)