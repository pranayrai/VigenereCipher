from flask import Flask, request, render_template
import vigenere_cipher
from genetic_algorithm import run_genetic_algorithm, decrypt_with_suitable_keywords

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    '''
        Approach: same as that of Caesar cipher listed above.
    '''
    if request.method == 'POST':
        plain_text = request.form['plain_text']
        keyword = str(request.form["keyword"])
        return render_template('vigenere.html', data=[plain_text, vigenere_cipher.encrypt(plain_text, keyword)])
    return render_template("vigenere.html", data=["", ""])

@app.route('/crack', methods=['GET','POST'])
def ga():
    '''
        render template and crack crypto system depending on choice of ciphers such as Caesar Cipher or Vigenere ciphers in our case!
    '''
    if request.method == 'POST':
        cipher_text = request.form['cipher_text']
        key_length = int(request.form['key_length'])
        num_of_generations = int(request.form['generations'])
        data = run_genetic_algorithm(key_length=key_length, cipher_text=cipher_text, number_of_generations=num_of_generations)
        data.append(cipher_text)
        data3 = decrypt_with_suitable_keywords(cipher_text)
        return render_template('crack.html', data=data, data3=data3)
    return render_template('crack.html')

if __name__ == '__main__':
	app.run()  