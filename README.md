# Chicago-Crime-Data-Analysis-and-Prediction

## Project Overview

Chicago Crime Data Analysis and Prediction is a Big Data Analytics project that leverages PySpark and Machine Learning to analyze historical crime records, identify crime patterns, and predict potential crime occurrences. The project helps law enforcement agencies and researchers gain insights into crime trends and high-risk areas through data-driven analysis and visualization.

## Objectives

- Analyze large-scale Chicago crime datasets using PySpark.
- Identify crime patterns based on location, time, and crime type.
- Predict crime occurrences using Machine Learning algorithms.
- Visualize crime hotspots through interactive heatmaps.

## Technologies Used

- Python
- PySpark
- Apache Spark
- Random Forest Classifier
- Pandas
- Matplotlib
- Folium
- Jupyter Notebook

## Project Structure

Chicago-Crime-Analysis/
│
├── dataset/
│   └── chicago_crimes.csv
│
├── notebooks/
│   └── crime_analysis.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── crime_analysis.py
│   ├── prediction_model.py
│   └── heatmap_visualization.py
│
├── output/
│   ├── crime_heatmap.html
│   ├── analysis_results.csv
│   └── prediction_results.csv
│
├── requirements.txt
└── README.md

## Workflow

1. Load Chicago crime dataset.
2. Clean and preprocess data.
3. Perform exploratory data analysis.
4. Extract relevant features.
5. Train a Random Forest prediction model.
6. Predict crime-related outcomes.
7. Generate crime hotspot heatmaps.
8. Visualize and interpret results.

## Features

- Large-scale crime data processing using PySpark.
- Crime trend analysis by type, location, and time.
- Machine learning-based crime prediction.
- Interactive crime hotspot visualization.
- Efficient handling of big datasets.

## Installation

Clone the Repository

git clone https://github.com/yourusername/chicago-crime-analysis.git
cd chicago-crime-analysis

Install Dependencies

pip install -r requirements.txt

Start Spark

Ensure Apache Spark and Java JDK are installed and configured.

## Usage

Run the analysis:

python crime_analysis.py

Run the prediction model:

python prediction_model.py

Generate heatmap:

python heatmap_visualization.py

## Results

- Identified high-crime areas and crime trends.
- Generated visual crime heatmaps.
- Predicted crime-related outcomes using Random Forest.
- Improved understanding of crime distribution across Chicago.


## Future Enhancements

- Real-time crime data integration.
- Deep Learning-based prediction models.
- Web dashboard for interactive monitoring.
- Mobile application support.
- Advanced geospatial analytics.

## References

1. Chicago Crime Dataset – City of Chicago Data Portal
2. Apache Spark Documentation
3. Machine Learning Research Papers on Crime Prediction

## Authors

- Nayan Poste

## Report
[Crime Data Analysis Report.pdf](https://github.com/user-attachments/files/29060663/Crime.Data.Analysis.Report.pdf)
