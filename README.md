# Combolist Creator by Eska

This Python script filters combos (formatted as `url:email:password`) from a file by a specified target site or domain. It extracts matching email:password pairs, displays them with color-coded output and progress bar, and saves the results to a timestamped file in a `results` folder.

---

## Features

- Filters combos containing a target site/domain in each line
- Extracts email and password pairs from matching lines
- Shows progress bar during processing with `tqdm`
- Colorful terminal output for better readability
- Saves filtered results automatically in a timestamped file
- Simple command-line interface

SCREEN:

![image](https://github.com/user-attachments/assets/3aa87119-2c35-410e-b6de-66885ad15837)

---

## Requirements

- Python 3.6+
- Python packages:
  - `tqdm`
  - `pyfiglet`
  - `termcolor`

Install dependencies with:

```bash
pip install tqdm pyfiglet termcolor
