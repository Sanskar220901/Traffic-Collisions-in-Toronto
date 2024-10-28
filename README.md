# Collision Insights - Web Application

---

## Project Overview

### Introduction
**Collision Insights** is an advanced data science web application developed using Python, Streamlit, and industry-standard data analytics libraries. Designed for city planners, traffic safety professionals, and insurance analysts, this application provides interactive dashboards that visualize motor vehicle collision patterns. Through deep integration with data processing techniques and interactive geospatial visualizations, **Collision Insights** enables stakeholders to monitor trends, identify high-risk areas, and derive actionable insights for public safety improvements and strategic resource allocation.

### Objectives
- **Insightful Data Exploration**: Enable data-driven insights into historical and geospatial collision trends, informing public safety strategies.
- **Predictive Analytics Foundation**: Lay the groundwork for predictive analysis and hotspot forecasting.
- **Intuitive User Experience**: Provide accessible, engaging visualizations for technical and non-technical stakeholders alike.

### Key Technologies and Concepts
- **Streamlit**: Provides an interactive framework for real-time data visualization.
- **pandas**: Supports data cleaning, transformation, and merging, central to preparing large datasets.
- **Plotly & pydeck**: Power interactive 2D and 3D geospatial visualizations.
- **Python**: Serves as the core language for data manipulation and visualization.
- **Data Science and Analytics Concepts**:
  - **Exploratory Data Analysis (EDA)**: Used to examine collision data and identify patterns.
  - **Geospatial Analysis**: Maps collision data for spatial risk assessment.
  - **Data Preprocessing**: Involves handling missing values, normalization, and outlier detection.

---

## Data Sources

### Data Ingestion and Preparation
The **Collision Insights** application integrates multiple datasets with yearly collision summaries and Key Safety Indicators (KSI). Primary data sources include:

- **Collisions_by_year.csv**: Contains annual collision data for trend analysis.
- **KSI.csv / KSI.xlsx**: Detailed records of individual collisions, including severity and road conditions.
- **KSI Macro.xlsm**: A macro-enabled Excel file with enriched data calculations, potentially including metrics such as fatality rates and injury severity.

### Data Dictionary
| Table Name                      | Column Name         | Data Type      | Description                                               |
|---------------------------------|---------------------|----------------|-----------------------------------------------------------|
| Collisions_by_year              | year               | Integer        | Year of data collection for trend analysis.               |
| Collisions_by_year              | collision_count    | Integer        | Total recorded collisions per year.                       |
| KSI                             | collision_id       | Integer        | Unique identifier for each collision.                     |
| KSI                             | location           | String         | Geographic coordinates (latitude, longitude).             |
| KSI                             | severity           | String         | Severity level (e.g., fatal, severe injury).              |
| KSI                             | collision_date     | Date           | Date of the collision event.                              |
| KSI Macro.xlsm                  | fatality_rate      | Float          | Calculated fatality rate per collision.                   |
| KSI Macro.xlsm                  | severity_index     | Integer        | Indexed measure of collision severity.                    |

### Data Quality and Governance
To maintain data integrity, **Collision Insights** applies the following practices:

- **Data Validation**: Ensures accuracy through type checks, handling missing values, and duplicate removal.
- **Data Provenance**: Logs ingestion and transformations to ensure traceability.
- **Compliance Standards**: Future production environments would implement RBAC and data anonymization.

---

## Application Architecture and Development

### Project Structure
**Collision Insights** follows a modular design, enabling efficient data flow from ingestion to visualization:

1. **Data Ingestion**:
   - Integrates sources in `CSV` and `Excel` formats with schema validation.
   - Batch processes high volumes of data for optimized loading.

2. **Data Cleansing and Transformation**:
   - Uses `pandas` to standardize data, handle null values, and format dates.
   - Prepares calculations in `KSI Macro.xlsm` to enrich severity metrics.

3. **Data Modeling and Feature Engineering**:
   - Creates features such as severity index and fatality rate for in-depth analysis.
   - Aggregates data by time, location, and severity level for efficient querying.

4. **Data Visualization**:
   - **Geospatial Mapping**: Maps collision data for spatial analysis.
   - **3D Visualization**: Adds depth to map views with collision density.
   - **Time-Series Charts**: Visualizes historical collision trends.

5. **User Interaction**:
   - Interactive filters allow users to explore data in real time.

### Application Flow in `app.py`
The workflow within `app.py` includes:

- **Data Loading**: Imports data using `pandas` with caching for efficiency.
- **Data Preprocessing**: Standardizes and joins data based on collision IDs.
- **Visualization Setup**: Uses `pydeck` for mapping and `Plotly` for charts.
- **User Customization**: Enables filters for real-time data exploration.

### Scalability and Extensibility
The application supports future scalability:

- **Cloud Integration**: Designed for compatibility with AWS S3 and Google Cloud Storage.
- **Real-Time Data Streaming**: Can integrate live data feeds from IoT sources.

---

## Technical Components and Best Practices

### Data Transformation and Modeling
- **Normalization**: Ensures consistent data formats.
- **Outlier Detection and Handling**: Flags anomalies in data.
- **Feature Engineering**: Calculates metrics like severity index and fatality rate.

### Security and Compliance
- **Role-Based Access Control (RBAC)**: Limits data access in production environments.
- **Data Masking**: Masks sensitive data to comply with GDPR and privacy standards.

### Performance Optimization
- **Data Caching**: Improves load times.
- **Optimized Aggregations**: Prepares data for efficient querying.

---

## Analysis and Visualization

### Analytical Strategy
The **Collision Insights** analytical framework applies spatial, temporal, and severity-based analysis:

- **Geospatial Analysis**: Maps high-risk zones.
- **Severity Analysis**: Uses severity index and fatality rate for risk assessment.
- **Temporal Trends**: Visualizes year-over-year collision trends.
- **Incident Density Mapping**: Uses 3D hexbin maps for dense collision areas.

### Interactive Dashboards and User Experience
- **Dynamic Filtering**: Filters by year, severity, and location.
- **Searchable Data Tables**: Detailed tables for granular analysis.
- **Customizable Visuals**: Visualizations allow trend analysis across metrics.

---

## Conclusion

### Summary of the Analysis
**Collision Insights** provides robust analytics for urban safety, equipping stakeholders with tools to assess collision trends and high-risk areas.

### Key Outcomes
- Created a data pipeline for processing large datasets.
- Developed user-friendly dashboards for public safety and risk assessment.
- Integrated geospatial analysis for hotspot identification and resource allocation.

### Future Enhancements
- **Predictive Analytics**: Introduce algorithms for future hotspot forecasting.
- **Real-Time Data Integration**: Integrate live data from traffic sensors.
- **Enhanced GIS Capabilities**: Provide overlays with road conditions.
- **Automated Reporting**: Enable CSV and PDF data exports.
- **Cloud Deployment**: Deploy on AWS or Google Cloud for scalability.

---

## Project Link
The **Collision Insights** code repository is available at: [https://github.com/Sanskar220901/Traffic-Collisions-in-Toronto].

## Dataset Link
The primary dataset is available at the Toronto Police Public Safety Data Portal:
https://data.torontopolice.on.ca/datasets/TorontoPS::ksi/about

---

## Contact Information
For further inquiries or collaboration opportunities, contact:

- **Email**: sanskarsrivastava2001@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/sanskar-srivastava-9074541a4/
- **GitHub**: https://github.com/Sanskar220901
- **Portfolio**: https://sanskarsrivastava.com/

---
