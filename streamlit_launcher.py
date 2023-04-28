import streamlit
import streamlit.web.bootstrap as bootstrap
import os

# configure streamlit using the environment variable instead of .streamlit/config.toml
# see also https://docs.streamlit.io/library/advanced-features/configuration
os.environ['STREAMLIT_SERVER_PORT'] = '8501'
# os.environ['STREAMLIT_GLOBAL_DEVELOPMENTMODE'] = 'false'

if __name__ == '__main__':
    # streamlit._is_running_with_streamlit = True
    print(f"os.environ['STREAMLIT_SERVER_PORT']: {os.environ['STREAMLIT_SERVER_PORT']}")
    bootstrap.run('main.py', 'streamlit run', (), {})