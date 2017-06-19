from flask import Flask, render_template, jsonify
from DbClass import DbClass

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/temp')
def temp():
    Dblayer = DbClass().gettempdate()

    datetemp = []

    for date in Dblayer:

        datetemp.append([str(date[0]), str(date[1])])

    return render_template('temp.html', data=datetemp)


@app.route('/druk')
def druk():
    Dblayer = DbClass().getdrukdate()

    datedruk = []

    for date in Dblayer:

        datedruk.append([str(date[0]), str(date[1])])

    return render_template('druk.html', data=datedruk)


@app.route('/vocht')
def vocht():
    Dblayer = DbClass().getvochtdate()

    datevocht = []

    for date in Dblayer:

        datevocht.append([str(date[0]), str(date[1])])

    return render_template('vocht.html', data=datevocht)


@app.route('/gdatatemp')
def tdata():
    Dblayer = DbClass().gettemp()

    temp = []

    for item in Dblayer:
        temp.append(str(item[0]))

    return jsonify({'result': temp})


@app.route('/gdatadruk')
def ddata():
    Dblayer = DbClass().getdruk()

    druk = []

    for item in Dblayer:
        druk.append(str(item[0]))

    return jsonify({'result': druk})


@app.route('/gdatavocht')
def dvocht():
    Dblayer = DbClass().getvocht()

    vocht = []

    for item in Dblayer:
        vocht.append(str(item[0]))

    return jsonify({'result': vocht})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
