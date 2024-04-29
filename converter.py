import requests
import tkinter as tk
from tkinter import ttk
import sv_ttk


# API key
api = "PASTE_YOUR_API_KEY_HERE"
# List of currencies
currencies = {
    "AED": "United Arab Emirates",
    "AFN": "Afghanistan",
    "ALL": "Albania",
    "AMD": "Armenia",
    "ANG": "Netherlands Antilles",
    "AOA": "Angola",
    "ARS": "Argentina",
    "AUD": "Australia",
    "AWG": "Aruba",
    "AZN": "Azerbaijan",
    "BAM": "Bosnia and Herzegovina",
    "BBD": "Barbados",
    "BDT": "Bangladesh",
    "BGN": "Bulgaria",
    "BHD": "Bahrain",
    "BIF": "Burundi",
    "BMD": "Bermuda",
    "BND": "Brunei",
    "BOB": "Bolivia",
    "BRL": "Brazil",
    "BSD": "Bahamas",
    "BTN": "Bhutan",
    "BWP": "Botswana",
    "BYN": "Belarus",
    "BZD": "Belize",
    "CAD": "Canada",
    "CDF": "Democratic Republic of the Congo",
    "CHF": "Switzerland",
    "CLP": "Chile",
    "CNY": "China",
    "COP": "Colombia",
    "CRC": "Costa Rica",
    "CUP": "Cuba",
    "CVE": "Cape Verde",
    "CZK": "Czech Republic",
    "DJF": "Djibouti",
    "DKK": "Denmark",
    "DOP": "Dominican Republic",
    "DZD": "Algeria",
    "EGP": "Egypt",
    "ERN": "Eritrea",
    "ETB": "Ethiopia",
    "EUR": "European Union",
    "FJD": "Fiji",
    "FKP": "Falkland Islands",
    "FOK": "Faroe Islands",
    "GBP": "United Kingdom",
    "GEL": "Georgia",
    "GGP": "Guernsey",
    "GHS": "Ghana",
    "GIP": "Gibraltar",
    "GMD": "The Gambia",
    "GNF": "Guinea",
    "GTQ": "Guatemala",
    "GYD": "Guyana",
    "HKD": "Hong Kong",
    "HNL": "Honduras",
    "HRK": "Croatia",
    "HTG": "Haiti",
    "HUF": "Hungary",
    "IDR": "Indonesia",
    "ILS": "Israel",
    "IMP": "Isle of Man",
    "INR": "India",
    "IQD": "Iraq",
    "IRR": "Iran",
    "ISK": "Iceland",
    "JEP": "Jersey",
    "JMD": "Jamaica",
    "JOD": "Jordan",
    "JPY": "Japan",
    "KES": "Kenya",
    "KGS": "Kyrgyzstan",
    "KHR": "Cambodia",
    "KID": "Kiribati",
    "KMF": "Comoros",
    "KRW": "South Korea",
    "KWD": "Kuwait",
    "KYD": "Cayman Islands",
    "KZT": "Kazakhstan",
    "LAK": "Laos",
    "LBP": "Lebanon",
    "LKR": "Sri Lanka",
    "LRD": "Liberia",
    "LSL": "Lesotho",
    "LYD": "Libya",
    "MAD": "Morocco",
    "MDL": "Moldova",
    "MGA": "Madagascar",
    "MKD": "North Macedonia",
    "MMK": "Myanmar",
    "MNT": "Mongolia",
    "MOP": "Macau",
    "MRU": "Mauritania",
    "MUR": "Mauritius",
    "MVR": "Maldives",
    "MWK": "Malawi",
    "MXN": "Mexico",
    "MYR": "Malaysia",
    "MZN": "Mozambique",
    "NAD": "Namibia",
    "NGN": "Nigeria",
    "NIO": "Nicaragua",
    "NOK": "Norway",
    "NPR": "Nepal",
    "NZD": "New Zealand",
    "OMR": "Oman",
    "PAB": "Panama",
    "PEN": "Peru",
    "PGK": "Papua New Guinea",
    "PHP": "Philippines",
    "PKR": "Pakistan",
    "PLN": "Poland",
    "PYG": "Paraguay",
    "QAR": "Qatar",
    "RON": "Romania",
    "RSD": "Serbia",
    "RUB": "Russia",
    "RWF": "Rwanda",
    "SAR": "Saudi Arabia",
    "SBD": "Solomon Islands",
    "SCR": "Seychelles",
    "SDG": "Sudan",
    "SEK": "Sweden",
    "SGD": "Singapore",
    "SHP": "Saint Helena",
    "SLE": "Sierra Leone",
    "SOS": "Somalia",
    "SRD": "Suriname",
    "SSP": "South Sudan",
    "STN": "São Tomé and Príncipe",
    "SYP": "Syria",
    "SZL": "Eswatini",
    "THB": "Thailand",
    "TJS": "Tajikistan",
    "TMT": "Turkmenistan",
    "TND": "Tunisia",
    "TOP": "Tonga",
    "TRY": "Turkey",
    "TTD": "Trinidad and Tobago",
    "TVD": "Tuvalu",
    "TWD": "Taiwan",
    "TZS": "Tanzania",
    "UAH": "Ukraine",
    "UGX": "Uganda",
    "USD": "United States",
    "UYU": "Uruguay",
    "UZS": "Uzbekistan",
    "VES": "Venezuela",
    "VND": "Vietnam",
    "VUV": "Vanuatu",
    "WST": "Samoa",
    "XAF": "CEMAC",
    "XCD": "Organisation of Eastern Caribbean States",
    "XDR": "International Monetary Fund",
    "XOF": "CFA",
    "XPF": "Collectivités d'Outre-Mer",
    "YER": "Yemen",
    "ZAR": "South Africa",
    "ZMW": "Zambia",
    "ZWL": "Zimbabwe" 
}

def convert(from_currency, to_currency, amount):
    url = f"https://v6.exchangerate-api.com/v6/{api}/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    print(data)
    conversion_rate = data["conversion_rates"][to_currency]
    conversion = round(conversion_rate * amount, 2)
    last_updated = data["time_last_update_utc"]
    return f"{amount} {from_currency} is equal to {conversion} {to_currency}\nLast updated: {last_updated}"

def on_convert_button_clicked():
    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()
    amount = amount_entry.get()
    
    if from_currency in currencies and to_currency in currencies and amount.replace('.', '', 1).isdigit():
        result = convert(from_currency, to_currency, float(amount))
        result_label.config(text=result)
    else:
        result_label.config(text="Please check your inputs and ensure amounts are numeric.")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# Create the input labels and entry fields
from_currency_label = ttk.Label(root, text="From Currency: (e.g. USD, EUR, GBP)")
from_currency_label.pack()
from_currency_entry = ttk.Combobox(root, values=list(currencies.keys()))
from_currency_entry.pack()

to_currency_label = ttk.Label(root, text="To Currency: (e.g. USD, EUR, GBP)")
to_currency_label.pack()
to_currency_entry = ttk.Combobox(root, values=list(currencies.keys()))
to_currency_entry.pack()

amount_label = ttk.Label(root, text="Amount:")
amount_label.pack()
amount_entry = ttk.Entry(root)
amount_entry.pack()

# Create the convert button
convert_button = ttk.Button(root, text="Convert", command=on_convert_button_clicked)
convert_button.pack()

# Create the result label
result_label = ttk.Label(root, text="")
result_label.pack()

# Apply the dark theme
sv_ttk.set_theme("dark")

# Start the main loop
root.mainloop()
