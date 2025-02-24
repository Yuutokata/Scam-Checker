
# Scam-Checker

This project is a school computer science project by Dominic and Leo. It aims to detect and warn users about potential online scams, phishing attacks, social engineering attempts, and viruses.

## How it Works

Scam-Checker utilizes various methods to analyze websites and determine their safety:

### 1. Phishing Database

A database of approximately 75,000 known phishing domains is used to identify potentially harmful websites. This database is free to use and was created by Leo. You can find it here: [https://github.com/Yuutokata/Phishing-Database](https://github.com/Yuutokata/Phishing-Database)

### 2. Google SafeBrowsing API

The project integrates with Google's SafeBrowsing API to detect malware, social engineering tactics, potentially dangerous websites, and unwanted software. For testing purposes, you can find URLs here: [https://testsafebrowsing.appspot.com/](https://testsafebrowsing.appspot.com/)

### 3. PyFunceble

The PyFunceble library is used to perform DNS lookups and check WHOIS records, providing additional information about website ownership and legitimacy. While we cannot provide specific URLs for testing this component, PyFunceble is a widely recognized and reliable library for these checks.

## Scoring System

Scam-Checker employs a scoring system from 0 to 100 to evaluate website safety. A score of 100 indicates the best rating, meaning the website is likely safe. Lower scores suggest potential risks, with 0 being the most dangerous.

## Educational Purpose

This project is primarily for educational purposes and is not intended for official or commercial use. It serves as a learning tool for understanding and implementing various scam detection techniques.

## Disclaimer

While Scam-Checker strives to provide accurate and reliable results, it cannot guarantee 100% accuracy in identifying all online threats. Users should always exercise caution and critical thinking when interacting with websites or online services.
