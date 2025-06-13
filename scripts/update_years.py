
# MIT License

# Copyright (c) 2025 Skillter (mix_skillter@protonmail.com) (https://skillter.dev) (github.com/Skillter)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



import datetime
import re

README_FILE = "README.md"

def update_years():
    """
    Grabs the readme file, and replaces how many years have passed since the specified year
    """
    try:
        with open(README_FILE, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"{README_FILE} not found")
        return

    ## get the specified year from the file
    pattern = re.compile(r"(<!-- AUTO_UPDATE_YEARS:(\d{4}) -->)(.*)(<!-- /AUTO_UPDATE_YEARS -->)")
    
    match = pattern.search(content)

    if not match:
        print("Marker not found in the readme file, add a marker like this:")
        print("<!-- AUTO_UPDATE_YEARS:2020 -->...<!-- /AUTO_UPDATE_YEARS -->")
        return

    start_year = int(match.group(2))
    current_year = datetime.datetime.now().year
    years_passed = current_year - start_year

    print(f"specified year: {start_year}, current year: {current_year}, years passed: {years_passed}")

    replacement_string = f"{match.group(1)}{years_passed}{match.group(4)}"
    
    updated_content = pattern.sub(replacement_string, content)

    # save the file
    with open(README_FILE, "w") as file:
        file.write(updated_content)

    print(f"Successfully updated {README_FILE}")

if __name__ == "__main__":
    update_years()