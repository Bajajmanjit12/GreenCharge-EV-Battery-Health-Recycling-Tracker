from flask import Flask, render_template, send_file
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('passport.html')  # First visit: shows button only

@app.route('/generate_passport')
def generate_passport():
    battery_info = {
        "Battery ID": "EVB-987654",
        "Manufacturer": "EcoVolt",
        "Charge Cycles": 540,
        "Voltage": "400V",
        "State of Health": "85%",
        "Last Updated": datetime.date.today().strftime("%Y-%m-%d")
    }

    # 1. Generate PDF
    pdf_filename = f"{battery_info['Battery ID']}_passport.pdf"
    pdf_path = os.path.join("static", pdf_filename)

    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "Battery Passport")

    c.setFont("Helvetica", 12)
    y = 710
    for key, value in battery_info.items():
        c.drawString(50, y, f"{key}: {value}")
        y -= 30

    # 2. Generate QR Code
    qr_url = f"http://127.0.0.1:5000/download/{pdf_filename}"
    qr_img = qrcode.make(qr_url)
    qr_path = os.path.join("static", "qr_codes", f"{battery_info['Battery ID']}_qr.png")
    os.makedirs(os.path.dirname(qr_path), exist_ok=True)
    qr_img.save(qr_path)

    # 3. Embed QR in PDF
    c.drawImage(qr_path, 400, 600, width=150, height=150)
    c.save()

    return render_template("passport.html", pdf=pdf_filename, qr=f"static/qr_codes/{battery_info['Battery ID']}_qr.png")

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join("static", filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
