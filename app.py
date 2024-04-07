from flask import Flask, render_template, request, redirect, flash, send_from_directory, url_for, session
import os
import ezdxf
import tempfile

app = Flask(__name__)
app.secret_key = "supersecretkey"

OUTPUT_FOLDER = 'output_files'
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

def process_dxf_to_oma(msp):
    oma_data = []
    for entity in msp:
        if entity.dxftype() == 'ARC':
            center = entity.dxf.center
            radius = entity.dxf.radius
            start_angle = entity.dxf.start_angle
            end_angle = entity.dxf.end_angle
            oma_data.append(f"ARC;CENTER({center[0]}, {center[1]});RADIUS({radius});ANGLE({start_angle}, {end_angle})")
    return "\n".join(oma_data)

@app.route('/download', methods=['GET'])
def download():
    filename = session.get('filename')
    if not filename:
        flash("No file to download!", "error")
        return redirect(url_for('index'))
    
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Nie wybrano pliku')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('Nie wybrano pliku')
            return redirect(request.url)

        # Zapisz plik tymczasowo
        temp_filename = tempfile.mktemp(suffix=".dxf")
        file.save(temp_filename)
        
        # Odczytaj plik tymczasowy
        doc = ezdxf.readfile(temp_filename)
        msp = doc.modelspace()
        
        oma_output = process_dxf_to_oma(msp)
        
        # Usuń plik tymczasowy
        os.remove(temp_filename)
        
        # Odczytaj dodatkowe informacje z formularza
        patient_name = request.form['patient_name']
        prescription_number = request.form['prescription_number']
        date = request.form['date']
        lens_type = request.form['lens_type']
        lens_material = request.form['lens_material']
        surface_treatment = request.form['surface_treatment']
        lens_color = request.form['lens_color']

        # Dodaj te informacje do wynikowego pliku OMA
        header = f"""
PATIENT_NAME={patient_name}
PRESCRIPTION_NUMBER={prescription_number}
DATE={date}
LENS_TYPE={lens_type}
LENS_MATERIAL={lens_material}
SURFACE_TREATMENT={surface_treatment}
LENS_COLOR={lens_color}
        """
        oma_output = header + oma_output

		  # Zapisz wynik do pliku
        filename = "output.oma"
        with open(os.path.join(OUTPUT_FOLDER, filename), 'w') as f:
            f.write(oma_output)

        # Ustaw nazwę pliku w sesji
        session['filename'] = filename
        
        # Ustaw komunikat dla użytkownika
        flash("Conversion successful! Click here to download your file.", "success")
        
        # Przekieruj do strony głównej
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
