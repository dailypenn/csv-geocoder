CSV Geocoder
================

Usage
---------------

This geocoder requires a Google API key. Set your API key using an environment variable:
```shell
export API_KEY=[your key]
```
(If you don't know what key to use, ask the Director of Web Development.)

You'll also need to install two modules: `pandas` and `googlemaps`.
```shell
pip install wheel
pip install pandas
pip install -U googlemaps
```

To run the program, make sure your input CSV file has a column called `address` and then run the following command in the same directory as `geocoder.py`:
```shell
python geocoder.py [file_name.csv]
```

The results will be output to a file called `geocoded_[file_name].csv` – the name of your original file with `geocoded_` prepended.

Notes
-------

This geocoder is used primarily for data at [The Daily Pennsylvanian](https://thedp.com). As such, it uses `Philadelphia` and `PA` as its city and state. If your data is for other cities/states, or has the city and state already included, adjust the code appropriately.

Credits
-------

Built by Alex Graves at [The Daily Pennsylvanian](https://thedp.com).
