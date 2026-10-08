# Rain Predictor flask app

Flask weather-input application serving rainfall predictions from a serialized machine-learning model.

## Repository guide

### Contents

- [Dockerfile](Dockerfile)
- [LICENSE](LICENSE)
- [Procfile](Procfile)
- [README.md](README.md)
- [Static](Static)
- [app.py](app.py)
- [first.png](first.png)
- [rain_XGBnew_model.pkl](rain_XGBnew_model.pkl)
- [requirements.txt](requirements.txt)
- [second.png](second.png)
- [template](template)
- [tests](tests)

### Getting started

```bash
git clone https://github.com/Raimal-Raja/Rain_Predictor_flask_app.git
cd Rain_Predictor_flask_app
```

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r "requirements.txt"
```

Application entry point:

```bash
python app.py
```

### Configuration and limitations

Regression tests use a mock predictor. Full inference still requires the serialized model and compatible training dependencies.

### Maintenance fixes

- Parse the date format produced by the HTML date input.
- Send a two-dimensional feature matrix to the predictor.
- Handle GET and invalid form input, and resolve models/static assets relative to the app.

### Validation

Reviewed on 2026-10-08. Two regression tests passed with unittest. Python source syntax checks passed. See tests/ for the tested behavior.

```bash
python -m unittest discover -s tests -v
```

### Contributions

Describe the issue, reproduction steps, environment, and expected behavior when proposing a change. Keep generated environments, credentials, and unnecessary build artifacts out of new commits.

### License

See [LICENSE](LICENSE) for the repository’s licensing terms.
