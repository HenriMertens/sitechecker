# Sitechecker

This script checks the status codes of sites or subdomains listed in a file.
Tested for kali linux, python3


## Installation

Clone the Repository


```bash
git clone https://github.com/HenriMertens/subdomain-checker.git 
```

## Usage
### Format file:
www.site.com  
www.example.com  
test.example.com  
...


### To run:
```bash
python3 domtester.py -F <file_path> -T <num_threads> -O 
```

### -F (required)
Filename, if file is in the same directory else file path 

### -T
Number of threads running (default = 50)
### -O
Only list sites that return status code 200
### -TO
Set timeout value



## License

[MIT](https://choosealicense.com/licenses/mit/)
