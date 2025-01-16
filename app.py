from flask import Flask, render_template, request # type: ignore
from math import comb

app = Flask(__name__)

# Fungsi untuk menghitung distribusi binomial
def binomial_probability(n, p, k):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Ambil input dari form
            n = int(request.form['n'])  # Jumlah total siswa
            p = float(request.form['p'])  # Probabilitas siswa berhenti
            k = int(request.form['k'])  # Jumlah siswa yang diprediksi berhenti

            # Hitung probabilitas binomial
            result = binomial_probability(n, p, k)
        except Exception as e:
            result = f"Error: {e}"

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=1024)
