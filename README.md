# DataPulse API

## Overview

The DataPulse API is a powerful and flexible RESTful API designed to provide real-time statistical analysis and visualization of data. It allows users to send data via WebSocket connections and receive insightful statistical metrics such as mean, median, standard deviation, and percentiles. This project is ideal for developers and data analysts looking to integrate robust data analysis capabilities into their applications.

## Features

- **Real-Time Data Analysis**: Send data through WebSocket connections and receive instant statistical metrics.
- **Statistical Metrics**: Get detailed statistics including mean, median, standard deviation, and percentiles.
- **Data Visualization**: (Planned for future versions) Generate visual representations of data.
- **Data Export**: (Planned for future versions) Export analysis results in various formats.

## Technologies Used

- **Python**: The programming language used for building the API.
- **FastAPI**: A modern web framework for building APIs with Python 3.6+.
- **WebSocket**: For real-time communication.
- **NumPy**: For numerical operations and statistical calculations.
- **pytest**: For testing and ensuring code quality.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lnpotter/DataPulse.git # or
   git clone https://github.com/yourusername/DataPulse.git # if you forked the repository
   cd DataPulse
   ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```
## Usage

1. **Upload Data**:
   - Endpoint: `/upload-data/`
   - Method: `POST`
   - Body: JSON array of data points.
   - Response: Mean value of the uploaded data.

2. **Get Graph**:
   - Endpoint: `/get-graph/`
   - Method: `POST`
   - Body: JSON array of data points and an optional `graph_type` parameter (default is "bar").
   - Response: Base64 encoded image of the generated graph.

3. **Export Data**:
   - Endpoint: `/export-data/`
   - Method: `POST`
   - Body: JSON array of data points and a `format` parameter (`csv` or `json`).
   - Response: Data in the specified format.

4. **Calculate Statistics**:
   - Endpoint: `/statistics/`
   - Method: `POST`
   - Body: JSON array of data points.
   - Response: Mean, median, standard deviation, and percentiles of the data.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/lnpotter/DataPulse/blob/main/LICENSE) file for more details.

