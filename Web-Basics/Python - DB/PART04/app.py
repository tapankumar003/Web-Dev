from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mypage')
def my_page():
   return 'HI, this is my page!'

@app.route('/hi')
def hi():
   return 'HI, boooooos!'

# @app.route('/test', methods=['GET'])
# def test_get():
#    title_receive = request.args.get('title_give')
#    print(title_receive)
#    return jsonify({'result':'success', 'msg': 'GET this request!'})

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': 'This request is POST!'})


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)