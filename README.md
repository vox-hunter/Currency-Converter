# Currency Converter App

## Overview
This Currency Converter application allows users to convert amounts between various global currencies. It utilizes the ExchangeRate-API for fetching real-time conversion rates. The user interface is built with Python and Tkinter, providing a straightforward and intuitive user experience with a sleek dark theme.

## Features
- **Currency Selection**: Choose from a comprehensive list of currencies for conversion.
- **Real-Time Conversion Rates**: Fetches the latest conversion rates from the ExchangeRate-API.
- **User-Friendly Interface**: Simple and clean GUI that supports easy navigation and operation.
- **Dark Theme**: Comfortable for the eyes, ideal for use in low-light environments.

## Demo
![Demo](https://github.com/vox-hunter/Currency-Converter/blob/main/Recording%202024-04-29%20194609.gif)

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.6 or higher
- Tkinter library
- `requests` library
- `sv_ttk` for styling

## How to get you API key:
- Go to [ExchangeRate-API](https://www.exchangerate-api.com/)
- Click "Get free key" button on top-right.
- then follow the steps shown on the website to get the api key
- after you get you api key do the following mentioned [here](#API-KEY)

## Installation

Clone the repository to your local machine:

- git clone https://github.com/vox-hunter/Currency-Converter.git
- cd your-project-directory

Install the required Python packages:

- pip install requests
- pip install sv_ttk

## API KEY
Ensure you replace `PASTE_YOUR_API_KEY_HERE` in the `api` variable inside `app.py` with your actual API key from ExchangeRate-API. Before you run the program


## Usage

Before you run the application, make sure you replace:
api = "PASTE_YOUR_API_KEY_HERE" with your own api key inside the double quotes (don't remove double quotes)

To run the application, execute the following command in the terminal:
python app.py

**Make sure you enter [**Three letter ISO currency code**](https://en.wikipedia.org/wiki/ISO_4217) or else it will give an error**

## Contributing

Contributions to enhance the functionality or performance of the Currency Converter are welcome. Please fork the repository and submit a pull request with your updates.

## Funding
Since this is a non-profit project, funding is appreciated at [Team Seas](https://teamseas.org/)

## License

This project is licensed under the Apache License - see the [LICENSE](https://github.com/vox-hunter/Currency-Converter/blob/main/LICENSE) file for details.

## Acknowledgments

- ExchangeRate-API for providing the currency conversion rates.
- Tkinter library for enabling the application's GUI.
- The [dark theme (sun valley) package](https://github.com/rdbende/Sun-Valley-ttk-theme) is by [Benedek Dévényi](https://github.com/rdbende)
- Thanks to Github Copilot to make coding faster

# Credits
Everything by [Vox Hunter](https://github.com/vox-hunter/)

