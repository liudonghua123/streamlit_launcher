# streamlit_launcher

## How to run it

1. `git clone https://github.com/liudonghua123/streamlit_launcher.git && cd streamlit_launcher`
2. `pipenv install` # install the dependences
3. `pipenv shell`   # activate venv
4. `python streamlit_launcher.py` # run the streamlit_launcher
5. `pyinstaller streamlit_launcher-onedir.spec --clean` # package as distribution directory
6. `pyinstaller streamlit_launcher-onefile.spec --clean` # package as single executable