# Scopus DPI documentation
## Checking the completeness of one author's collection
### Prerequisites
You need a file `NTU_DOI.csv`, and DR-NTU DOI link as the third column
You need a machine with Python3, preferably Python 3.6.6 installed.
Install `imp`, `requests`, and `pandas` and `scopus` using `pip3` install.
For newly installed python3, you may also need to install pbr if you encounter the below error:
```bash
Command "python setup.py egg_info" failed with error code 1 in /private/var/folders/r8/2tmjwrx168ggntqdhtqf7sgc0000gp/T/pip-install-srbso_i8/scopus/
```
### Steps
Clone this repository to get the code.
Put the `NTU_DOI.csv` file in the repository root directory.
Run the following
``` bash
python3 getAuthorDOI.py
python3 extractDOIfromDRNTU.py
python3 compare.py
```
The desired result would be in the file `compareResult.csv`
## Troubleshooting
### `configparser.DuplicateSectionError: Section 'Warnings' already exists` error.

Here is an example of the error log
``` bash
    "D:/PhD/Projects/Code/scopus/main.py"
Traceback (most recent call last):
  File "D:/PhD/Projects/Code/scopus/main.py", line 1, in <module>
    import scopus
  File "C:\Users\myUser\AppData\Local\Continuum\anaconda3\lib\site-packages\scopus\__init__.py", line 7, in <module>
    from scopus.utils import *
  File "C:\Users\myUser\AppData\Local\Continuum\anaconda3\lib\site-packages\scopus\utils\__init__.py", line 1, in <module>
    from scopus.utils.create_config import *
  File "C:\Users\myUser\AppData\Local\Continuum\anaconda3\lib\site-packages\scopus\utils\create_config.py", line 5, in <module>
    from scopus.utils.startup import config, CONFIG_FILE
  File "C:\Users\myUser\AppData\Local\Continuum\anaconda3\lib\site-packages\scopus\utils\startup.py", line 23, in <module>
    config.add_section('Warnings')
  File "C:\Users\myUser\AppData\Local\Continuum\anaconda3\lib\configparser.py", line 1200, in add_section
    super().add_section(section)
  File "C:\Users\myUser\AppData\Local\Continuum\anaconda3\lib\configparser.py", line 659, in add_section
    raise DuplicateSectionError(section)
configparser.DuplicateSectionError: Section 'Warnings' already exists
```
Notice the line with `scopus\utils\startup.py", line 23`. Follow the file path and comment that line 23. It should resolve the problem.

### `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)` error
For UNIX based system, delete the whole content of the `~/.scopus/` directory except the file `config.ini`. The problem should be caused because of false caching (the library believe that it was cached probably but turns out the cache is empty)

### `with open(qfile, 'wb') as f: FileNotFoundError: [Errno 2] No such file or directory: '/Users/DPI/.scopus/author_retrieval/18439033600'`
Delete the whole `~/.scopus/' directory. Uninstall the scopus using `pip3 uninstall scopus` and reinstall.

### `UserWarning: scopus did not find a configuration file`
Run the python3 bash, then
``` python
import scopus
scopus.utils.create_config()
```
Enter your credentials.
