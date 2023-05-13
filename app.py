import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout='wide')

# Loading the Data URL
DATA_URL = (
    "KSI.csv"
)


#Heading of Page
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'> Exploratory Analysis - Traffic Collisions in Toronto (2006 - 2022) </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'> Sanskar Srivastava </h4>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)



#Intro Section

st.markdown("<p style='text-align: center;'> The website is a Streamlit dashboard that provides insights on motor vehicle collisions in Toronto from 2006 to 2022. The dataset includes all traffic collisions where a person was either killed or seriously injured (KSI). The dashboard offers various interactive tools for data analysis, such as a map that shows the exact locations of KSI cases in Toronto categorized by the unique neighborhood ID setup by City of Toronto, and a slider to choose the year to analyze the trend of motor vehicle collisions. Additionally, it provides information on the number of KSI cases by hour of day and age group, helping users identify the peak hour and age group with the highest number of victims. The website is useful for people who are interested in analyzing the trends and patterns of motor vehicle collisions in Toronto.</p>", unsafe_allow_html=True)



#Data Loading
@st.cache_data(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data['HOOD_174'] = pd.to_numeric(data['HOOD_174'], errors='coerce').fillna(0)
    data.dropna(subset=['LATITUDE', 'LONGITUDE', 'INVAGE', 'HOOD_174'], inplace=True)
    return data

data = load_data(18194)

st.markdown("<h2 style='text-align: center;'>Sample Data</h2>", unsafe_allow_html=True)

st.write(data.head())

st.markdown("<p style='text-align: right;'>© Toronto Police Service</p>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)



#Neighbourhood Section

st.markdown("<h2 style='text-align: center;'> Killed or Seriously Injured (KSI) Cases in Toronto by Neighbourhood</h2>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'>Please use the slider below to choose the unique ID for City of Toronto neighbourhood(s) between <b>1</b> to <b>174</b>.</h5>", unsafe_allow_html=True)

neighbourhood = st.slider("",1, 174)

st.map(data.query("HOOD_174 == @neighbourhood")[["LATITUDE", "LONGITUDE"]].dropna(how="any"))
data_neighbourhood = data[data['HOOD_174'] == neighbourhood]

if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(data_neighbourhood)




#Neighbourhood Section - Analysis
st.markdown("<p style='text-align: center;'> The map shows the exact location of where the Killed or Seriously Injured (KSI) cases occurred in Toronto categorized by the unqiue neighbourhood ID setup by City of Toronto. The map gives insights about which neighbourhoods are more prone to motor vehicle collisions. The user can zoom in and zoom out of the map to change the view. <br> Between 2006 and 2022, <b>neighbourhood 1 ('West Humber-Clairville')</b> had the most number of collisions of <b>487</b> and <b>neighbourhood 29 ('Maple Leaf')</b> had the least number of collisions of just <b>15</b>. <br> The 'Show Raw Data' checkbox helps to view the data points in a tabular format. The table is dynamically sorted according to the unique neighbourhood ID ('HOOD_174' column in table) selected using the slider. The name of the neighbourhood can be seen in the corresponding 'NEIGHBOURHOOD_174' column in the table.   </p>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)




#Collisions by Year
st.markdown("<h2 style='text-align: center;'> Motor Vehicle Collisions by Year</h2>", unsafe_allow_html=True)

data_by_year = {'YEAR': ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
        'COLLISIONS': [1155, 1113, 969, 969, 920, 906, 1010, 1001, 883, 904, 979, 951, 1018, 907, 611, 612, 677]
}

st.markdown("<h5 style='text-align: center;'> Number of Killed or Seriously Injured (KSI) cases by year.</h5>", unsafe_allow_html=True)




#Data Loading - Line Graph
df1 = pd.DataFrame(data_by_year)



# Create a function that will display the line graph
def show_line_graph(data_by_year):
    fig = px.line(df1, x='YEAR', y='COLLISIONS', markers=True)
    st.plotly_chart(fig, use_container_width=True)
show_line_graph(data_by_year)




#Collisions by Year - Analysis
st.markdown("<p style='text-align: center;'> Based on the trend, the number of motor vehicle collisions gradually reduced from <b>1155 in 2006</b> to <b>677 in 2022</b> with an average decline in motor vehicle collisions of <b>4.17%</b> yearly. </p>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)


st.markdown("<h5 style='text-align: center;'>Please use the slider below to change the year.</h5>", unsafe_allow_html=True)
year = st.slider("", 2006, 2022)
st.map(data.query("YEAR == @year")[["LATITUDE", "LONGITUDE"]])
data_year = data[data['YEAR'] == year]

if st.checkbox("Show Raw Data ", False):
    st.subheader('Raw Data')
    st.write(data_year)


st.markdown("<p style='text-align: center;'> The map provides the locations of motor vehicle collisions that occurred in a particular year which can be used to analyze the trends of collisions from one year to another. The user can zoom in and zoom out of the map to change the view. <br> The 'Show Raw Data' checkbox displays the data points in a tabular format.  The table is dynamically sorted according to the year ('YEAR' column in table) selected using the slider.   </p>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)




#Collisions by Hour of Day
st.markdown("<h2 style='text-align: center;'>Motor Vehicle Collisions During Given Hour of Day</h2>", unsafe_allow_html=True)



# Collision by Hour of Day - Line Graph
data_by_hour = {'HOUR': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'],
        'NUMBER OF COLLISIONS': ['343', '758', '1044', '512', '1245', '2856', '3416', '4696', '5751', '6490', '7414', '8412', '9971', '12040', '14115', '15040', '17476', '19242', '17556', '16860', '16380', '15334', '12857']
}

st.markdown("<h5 style='text-align: center;'> Number of Killed or Seriously Injured (KSI) cases by hour of day.</h5>", unsafe_allow_html=True)




#Data Loading - Line Graph
df2 = pd.DataFrame(data_by_hour)



# Create a function that will display the line graph
def show_line_graph_hour(data_by_hour):
    fig2 = px.line(df2, x='HOUR', y='NUMBER OF COLLISIONS', markers=True)
    st.plotly_chart(fig2, use_container_width=True)
show_line_graph_hour(data_by_hour)


#Collisions by Hour of Day - Analysis
st.markdown("<p style='text-align: center;'>The number of Killed or Seriously Injured (KSI) cases by hour was at peak during the 18th hour (6:00 PM - 7:00 PM). </p>", unsafe_allow_html=True)



#Collisions by Hour of Day - Map
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>Location of Motor Vehicle Collisions During Given Hour of Day</h2>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'>Please use the slider below to change the hour of the day</h5>", unsafe_allow_html=True)
hour = st.slider("", 0, 24)
data_hour = data.query("HOUR == @hour")

st.markdown("<p style='text-align: center;'>Vehicle Collisions between <b>%i:00</b> and <b>%i:00</b> </p>" % (hour, (hour+1)), unsafe_allow_html=True)

midpoint = (np.average(data['LATITUDE']), np.average(data['LONGITUDE']))

st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/navigation-night-v1",
    initial_view_state={
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11,
        "pitch": 50,
    },
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=data_hour[['HOUR', 'LATITUDE', 'LONGITUDE']],
            get_position=['LONGITUDE', 'LATITUDE'],
            radius=100,
            extruded = True,
            pickable = True,
            elevation_scale=4,
            elevation_range=[0, 1000],
        ),
    ],
))



if st.checkbox("Show Raw Data  ", False):
    st.subheader('Raw Data')
    st.write(data_hour)




#Collisions by Hour of Day - Analysis

st.markdown("<p style='text-align: center;'> The map shows the distribution of Killed or Seriously Injured (KSI) cases across Toronto during a given hour of the day. <br> The size and colour of the hexagonal cylinder is proportional to the number of motor vehicle collisions in that particular location. </p>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)




#KSI by Year & Age Group - histogram

st.markdown("<h2 style='text-align: center;'>Number of Killed or Seriously Injured (KSI) cases each year in Toronto <br>(by Age Group)</h2>", unsafe_allow_html=True)

data_age = {'AGE_GROUP': ['0 to 4', '5 to 9', '10 to 14', '15 to 19', '20 to 24', '25 to 29', '30 to 34',
                      '35 to 39', '40 to 44', '45 to 49', '50 to 54', '55 to 59', '60 to 64', '65 to 69',
                      '70 to 74', '75 to 79', '80 to 84', '85 to 89', '90 to 94', 'Over 95'],
        '2006': [17, 21, 20, 97, 128, 121, 96, 91, 130, 96, 83, 68, 46, 37, 29, 30, 26, 11, 4, 4],
        '2007': [15, 23, 18, 66, 111, 104, 99, 120, 106, 110, 73, 82, 54, 27, 44, 28, 20, 8, 5, 0],
        '2008': [8, 7, 12, 47, 107, 106, 84, 87, 87, 80, 93, 55, 57, 38, 32, 25, 19, 21, 4, 0],
        '2009': [13, 9, 10, 52, 122, 90, 85, 91, 103, 81, 79, 64, 49, 33, 21, 20, 26, 16, 5, 0],
        '2010': [6, 11, 10, 52, 97, 102, 83, 78, 92, 83, 80, 67, 34, 27, 28, 33, 20, 13, 4, 0],
        '2011': [8, 7, 13, 46, 74, 105, 69, 70, 88, 86, 90, 67, 44, 38, 38, 30, 17, 13, 3, 0],
        '2012': [9, 4, 12, 29, 117, 107, 90, 88, 71, 108, 100, 65, 55, 50, 33, 34, 17, 20, 1, 0],
        '2013': [9, 15, 19, 43, 102, 103, 81, 88, 82, 71, 99, 69, 52, 52, 38, 32, 25, 14, 5, 2],
        '2014': [4, 12, 15, 56, 99, 108, 74, 74, 69, 58, 73, 50, 68, 42, 22, 23, 21, 10, 5, 0],
        '2015': [16, 20, 54, 101, 75, 74, 72, 67, 72, 18, 68, 63, 55, 47, 33, 24, 20, 19, 6, 0],
        '2016': [7, 18, 54, 120, 102, 88, 70, 65, 53, 16, 80, 78, 63, 61, 39, 30, 18, 10, 4, 3],
        '2017': [18, 12, 61, 100, 98, 86, 81, 48, 71, 15, 67, 84, 65, 50, 38, 23, 16, 13, 3, 2],
        '2018': [16, 21, 34, 119, 110, 97, 64, 71, 86, 8, 99, 77, 52, 40, 39, 36, 27, 17, 4, 1],
        '2019': [13, 18, 55, 102, 100, 78, 74, 63, 62, 12, 79, 58, 56, 47, 33, 22, 25, 7, 1, 2],
        '2020': [4, 13, 22, 63, 74, 66, 60, 41, 37, 6, 59, 46, 46, 25, 21, 13, 9, 4, 2, 0],
        '2021': [6, 6, 49, 71, 57, 67, 52, 38, 42, 8, 38, 49, 41, 31, 22, 14, 13, 7, 1, 0],
        '2022': [8, 12, 35, 79, 76, 68, 53, 53, 43, 7, 42, 56, 40, 36, 19, 17, 17, 9, 6, 1]
}

df = pd.DataFrame(data_age)

    
st.markdown("<h5 style='text-align: center;'>Please use the dropdown below to change the year</h5>", unsafe_allow_html=True)

date_year = st.selectbox("", options=["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"])



# Create a function that will display the histogram
def show_histogram(date_year):
    fig = px.histogram(df, x='AGE_GROUP', y=date_year, labels = {'AGE_GROUP': 'Age Group', date_year: 'Killed or Seriously Injured (KSI) cases'}, title=f"Number of People Killed or Seriously Injured (KSI) in {date_year} by Age Group")
    st.plotly_chart(fig, use_container_width=True)
show_histogram(date_year)


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Cumulative Number of Killed or Seriously Injured (KSI) cases in Toronto <br>(by Age Group)</h2>", unsafe_allow_html=True)




#KSI by Year & Age Group - line graph
collisions_by_age_group = {'AGE GROUP': ['0 to 4', '5 to 9', '10 to 14', '15 to 19', '20 to 24', '25 to 29', '30 to 34',
                      '35 to 39', '40 to 44', '45 to 49', '50 to 54', '55 to 59', '60 to 64', '65 to 69',
                      '70 to 74', '75 to 79', '80 to 84', '85 to 89', '90 to 94', 'Over 95'],
                      'TOTAL COLLISIONS': [177, 199, 249, 852, 1712, 1638, 1385, 1313, 1274, 1239, 1302, 1098, 877, 681, 529, 434, 336, 212, 63, 15]
                      }


#Data Loading - Line Graph
df3 = pd.DataFrame(collisions_by_age_group)


# Create a function that will display the line graph
def show_line_graph_age(collisions_by_age_group):
    fig3 = px.line(df3, x='AGE GROUP', y='TOTAL COLLISIONS', markers=True)
    st.plotly_chart(fig3, use_container_width=True)
show_line_graph_age(collisions_by_age_group)



st.markdown("<p style='text-align: center;'> Based on the line graph, we can conclude that the highest amount of victims of Killed or Seriously Injured (KSI) cases belong to the age group <b>20 to 24</b>. </p>", unsafe_allow_html=True)


st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'> References: </h5>", unsafe_allow_html=True)


st.markdown("<a style='text-align: center; href = 'https://data.torontopolice.on.ca/datasets/TorontoPS::ksi/about'> Toronto Police Service - Public Safety Data Portal </a>", unsafe_allow_html=True)


