# EV Sales Data Analysis

This project is an analysis of electric vehicle (EV) sales data in the United States. The goal of the analysis is to identify trends and patterns in the data that can help us understand the EV market better. The project includes two main scripts: `summary.py` and `dataMining.py`.

## Getting Started

To get started with this project, you will need to have Python 3.x installed on your computer. You will also need to download the EV sales data set, which is available in CSV format [here](https://www.kaggle.com/joshuajhchoi/ev-sales-data).

## Project Structure

-   `summary.py`: This script provides a summary of the EV sales data, including total sales by year and by state, top-selling EV models, and a breakdown of sales by vehicle class.
    
-   `dataMining.py`: This script performs data mining on the EV sales data using clustering analysis to identify which vehicle makes are most common in each state.
    
-   `main.py`: This script provides a terminal user interface for launching either `summary.py` or `dataMining.py`.
    

## Running the Scripts

To run the `summary.py` or `dataMining.py` scripts, you can simply execute the script in a Python environment. For example:

pythonCopy code

`python summary.py`

To run the `main.py` script, you can execute the script in a Python environment and follow the prompts:

pythonCopy code

`python main.py`

## Dependencies

This project requires the following Python libraries:

-   pandas
-   sklearn
-   matplotlib

You can install these libraries using `pip`:

pythonCopy code

`pip install pandas sklearn matplotlib`

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://chat.openai.com/LICENSE.md) file for details.
