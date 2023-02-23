
from  flask  import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('1.html')

@app.route("/login",methods=['post']) 
def login():
    keyword = ''
    keyword2 = ''
    ciphertext = request.form.get('ciphertext')
    keyword = request.form.get('keyword')
    plaintext2 = request.form.get('plaintext')
    keyword2 = request.form.get('keyword2')
    print('key1=',keyword,
          'key2=',keyword2)
    # decrypt
    def vigenere_decrypt(ciphertext, keyword):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        keyword = keyword.upper()
        ciphertext = ciphertext.upper()
        plaintext = ""
        for j, char in enumerate(ciphertext):
            if char in alphabet:
                shift = alphabet.index(keyword[j % len(keyword)])
                new_char_index = (alphabet.index(char) - shift + 26) % 26
                new_char = alphabet[new_char_index]
                plaintext += new_char
            else:
                plaintext += char
        return plaintext
    decrypted_text = vigenere_decrypt(ciphertext, keyword)

    # encrypt
    def vigenere_encrypt(plaintext2, keyword2):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        keyword2 = keyword2.upper()
        plaintext2 = plaintext2.upper()
        ciphertext2 = ""
        for j, char in enumerate(plaintext2):
            if char in alphabet:
                shift = alphabet.index(keyword2[j % len(keyword2)])
                new_char_index = (alphabet.index(char) + shift) % 26
                new_char = alphabet[new_char_index]
                ciphertext2 += new_char
            else:
                ciphertext2 += char
        return ciphertext2
    encrypted_text = vigenere_encrypt(plaintext2, keyword2)
    print('d=',decrypted_text,'e=',encrypted_text)

    if keyword != '':   # Something for decrypt
        print('decrypt')
        return render_template('2.html', msg = decrypted_text)
    else:    # Nothing input for decrypt, then encrypt
        print('encrypt')
        return render_template('3.html', msg = encrypted_text)

if __name__ == '__main__':
    app.run()
