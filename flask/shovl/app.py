import os

from flask import Flask, render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def index():
        techs = [
            'Cloud Services',
            'Artificial Intelligence/Machine Learning',
            'Internet of Things',
            'Augmented Reality/Virtual Reality',
            'Cybersecurity',
            'Big Data/Analytics',
            'Blockchain',
            'Robotics/Industrial Automation',
            'Digital Marketing/Advertising',
            'FinTech',
            'HealthTech/MedTech',
            'Telecommunications',
            'Renewable Energy',
            '3D Printing/Additive Manufacturing',
            'Quantum Computing',
            'Biotechnology',
            'Nanotechnology',
            'Aerospace and Defense'
        ]
        return render_template('index.html', techs=techs)

    return app