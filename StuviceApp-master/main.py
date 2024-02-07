from website import create_app
import logging


app = create_app()
app.logger.setLevel(logging.DEBUG)

@app.route('/google_fonts')
def google_fonts():
    return 'https://fonts.googleapis.com/css?family=Lato:300,400,400i,700,700i'

google_fonts()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug = True)

    #app.run(debug=True)
