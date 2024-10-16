### Code-AuditX

Code-AuditX is a python script that scans a directory, analyzes its files, and  provides a summary of each file's type, total file size and total number of files. It is useful for quickly gathering insights about the contents of a folder, including extensions commonly used in **Forensics** and **Cybersecurity**.

---------------------------------------------------

### Tech Used

- Python 3.x
- OS Library

---------------------------------------------------

### Features

- Detects file types based on extensions (Python, Assembly, Windowss DLL etc).
- Calculates and displays the total size of each file in bytes.
- Groups files by their extension and language.
- Supports extensions related to Digital Forensics (.pcap, .exe, .dmp, .ps1 etc).
- Provides a summary of total files and total size for each language and extension.

---------------------------------------------------

### Code Example

##### Example Directory
````
PS D:\>cd code-auditx
````
##### Example Output
![Example Output 1](https://github.com/I-am-Rudy/code-auditx/blob/main/1.png)

![Example Output 2](https://github.com/I-am-Rudy/code-auditx/blob/main/2.png)

---------------------------------------------------

### Installations

1. Clone the repository:
````
git clone https://github.com/username/code-audtix.git
````

2. Navigate to the project directory:
````
cd code-auditx
````

3. Ensure Python 3 is installed:
Also install required dependencies with
````
pip install -r requirements.txt
````

---------------------------------------------------

### How to Use

1. Run the script from the terminal:
````
python code-auditx.py
````

2. When prompted, enter the path to the directory you want to analyze:
````
Enter the directory path : C:\Windows
````

3. The script will analyze the directory and display the file information:
(image of output)

---------------------------------------------------

### License

This project is licensed under the MIT license - see https://www.gnu.org/licenses/agpl-3.0.en.html file for details
