# House Price Calculator

A tool to calculate house prices based on various features using Python and machine learning.

## Features
- Basic CLI calculator
- Sample data
- Machine learning model (scikit-learn)

## Requirements
- Python 3.x
- Install dependencies with:
  ```bash
  pip install -r requirements.txt
  ```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/arsalan-test/house-price-calculator.git
   cd house-price-calculator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the CLI tool with your own values for area, bedrooms, and age:
   ```bash
   python house_price_calculator.py <area> <bedrooms> <age>
   ```
   Example:
   ```bash
   python house_price_calculator.py 2000 3 10
   ```
   This will output the predicted house price based on the trained model and your input.

## Files
- `house_price_calculator.py`: Main CLI tool
- `sample_data.csv`: Sample data for training
- `requirements.txt`: Python dependencies

## License
MIT
