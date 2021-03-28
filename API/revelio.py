from flask import Flask, jsonify
import CVESearch, SerialNumberSearch

app = Flask(__name__)

@app.route("/search/<vendor>/<product>", methods=["GET"])
def getSearch( vendor, product ):
	vendor = str(vendor)
	product = str(product)
	return jsonify( CVESearch.getCVEs( vendor, product ) )
	
@app.route("/browse/<vendor>", methods=["GET"])
def getVendor( vendor ):
	vendor = str(vendor)
	return CVESearch.getProductsByBrand( vendor )
	
@app.route("/find/netgear/<serialnumber>", methods=["GET"])
def getNetgearSerialNumber( serialnumber ):
	serialnumber = str(serialnumber)
	return SerialNumberSearch.getNetGearProduct( serialnumber )

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8080, debug=True)
