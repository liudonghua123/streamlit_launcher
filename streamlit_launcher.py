# import streamlit
import streamlit.web.bootstrap as bootstrap
from streamlit.config import get_config_options, set_option
import os
import sys

# configure streamlit using the environment variable instead of .streamlit/config.toml
# see also https://docs.streamlit.io/library/advanced-features/configuration
# os.environ['STREAMLIT_SERVER_PORT'] = '8501'
# os.environ['STREAMLIT_GLOBAL_DEVELOPMENTMODE'] = 'false'

if __name__ == '__main__':
    # streamlit._is_running_with_streamlit = True
    # print(f"env STREAMLIT_SERVER_PORT: {os.environ['STREAMLIT_SERVER_PORT']}, STREAMLIT_GLOBAL_DEVELOPMENTMODE: {os.environ['STREAMLIT_GLOBAL_DEVELOPMENTMODE']}")
    set_option('server.port', os.environ.get('STREAMLIT_SERVER_PORT') or 8501)
    set_option('global.developmentMode', False)
    # config = get_config_options(force_reparse=True)
    # print(f'config: {config}')
    main_script_path = 'main.py'
    if len(sys.argv) > 1:
        main_script_path = sys.argv[1]
    bootstrap.run(main_script_path, f'streamlit run {main_script_path}', (), {})