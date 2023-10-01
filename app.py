from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def input_page():
    if request.method == 'POST':
        # Retrieve form data
        data = request.json
        sites = int(data['sites'])
        processes = [int(p) for p in data['processes']]
        s1 = int(data['s1'])
        p1 = int(data['p1'])
        sp1 = int(data['sp1'])
        sp2 = int(data['sp2'])

        # Perform calculations
        deadlock_detected = False
        probe_msg = f"\nProbe message is ({p1}, {sp1}, {sp2})"
        if p1 == sp2:
            deadlock_detected = True

        # Return the result as JSON
        return jsonify(deadlock_detected=deadlock_detected,probe_msg=probe_msg)

    # Render the input page template
    return render_template('input.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
