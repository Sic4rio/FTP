# FTP Anonymous Login Checker

![Developed on Kali Linux](https://img.shields.io/badge/Developed%20on-Kali%20Linux-557C94?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A Python script to check for anonymous login on FTP servers.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Prerequisites](#prerequisites)
- [Running the Script](#running-the-script)
- [Author](#author)
- [License](#license)

## Introduction

This script is designed to check for anonymous login access on FTP servers. It takes a list of target IP addresses as input and attempts to log in anonymously to each FTP server. If successful, it reports a successful login; otherwise, it marks the login attempt as failed.

## Usage

To use this script, follow the instructions below.

### Prerequisites

- Python 3.x
- `colorama` library (you can install it using `pip install colorama`)

### Running the Script

1. Clone the repository or download the script file.

2. Open a terminal or command prompt on your Kali Linux system.

3. Navigate to the directory containing the script.

4. Run the script using the following command:

   ```bash
   python ftp_anon_checker.py -u [URL or file path]

