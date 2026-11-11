# YallaKora Matches Scraper ⚽

## 📌 Project Overview
A Python-based web scraping project that extracts football match information from [YallaKora](https://www.yallakora.com/) based on a user-specified date.

The scraper collects match details from different championships and exports the extracted data into a CSV file for further analysis.

## 🚀 Features
- Extract matches for a specific date.
- Retrieve championship names and match rounds.
- Extract participating team names.
- Get match schedules and kick-off times.
- Retrieve match scores when available.
- Identify matches that have not been played yet.
- Export collected data into a structured CSV file.

## 🛠️ Technologies & Libraries
- **Python** – Main programming language.
- **Requests** – Sending HTTP requests and retrieving webpage content.
- **BeautifulSoup4** – Parsing HTML and extracting match information.
- **lxml** – HTML parser.
- **CSV** – Exporting extracted data into CSV files.

## 📂 Extracted Data
The scraper collects the following information:

| Field | Description |
|---|---|
| البطولة | Championship Name |
| الجولة | Match Round |
| التاريخ | Match Date |
| الوقت | Match Time |
| الفريق الأول | First Team |
| الفريق الثاني | Second Team |
| النتيجة | Match Score |

## ⚙️ Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/mo-f-alfaraj/Catch_Matches_Schedule.git
```

**2. Install the required libraries**
```bash
pip install requests beautifulsoup4 lxml
```

## ▶️ How to Run

Run the Python script:

```bash
python main.py
```

Enter the desired date when prompted using the following format:

```text
MM/DD/YYYY
```

Example:
```text
11/11/2026
```

The extracted match data will be saved as a CSV file.

## 📊 Output
The project generates a CSV file containing the extracted match information, with UTF-8 encoding support for Arabic text.

Example filename:
```text
Matches_11-11-2026.csv
```

## 🔮 Future Improvements
- Add error handling for failed HTTP requests.
- Improve data extraction reliability.
- Make the output directory configurable.
- Add support for automated data collection.
- Integrate Pandas for further data processing and analysis.

## 👨‍💻 Author
**Mohammed Fathy**

[GitHub Profile](https://github.com/mo-f-alfaraj)
