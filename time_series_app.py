Simport pandas as pd
import numpy as np
import os
from PIL import Image

# first line after the importation section
st.set_page_config(page_title="Demo app", page_icon="🐞", layout="centered")
DIRPATH = os.path.dirname(os.path.realpath(__file__))


@st.cache_resource()  # stop the hot-reload to the function just bellow
def setup(tmp_df_file):
    "Setup the required elements like files, models, global variables, etc"
    pd.DataFrame(
        dict(
            firstname=[],
            laststname=[],
            gender=[],
            special_date=[],
            comment=[],
            height=[],
        )
    ).to_csv(tmp_df_file, index=False)


tmp_df_file = os.path.join(DIRPATH, "tmp", "data.csv")
setup(tmp_df_file)


image = Image.open('time.png')
st.title('📈 Time Series Forecasting')

st.sidebar.write(f"This data app is an interface for a Grocery Store Sales Forecast Model  developed from data from an Ecuadorian Grocery Store.")

form = st.form(key="information", clear_on_submit=True)

# Step 1: Import Data
df = st.file_uploader('Import the time series csv file here.')

### Step 2: Select Forecast Horizon


periods_input = st.number_input('How many periods would you like to forecast into the future?',
min_value = 1, max_value = 365)
