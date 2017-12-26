from flask import Flask, jsonify
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient().gdax_trader

@app.route('/engine/heartbeat')
def get_heartbeat():
    return jsonify(client.engine.find({'heartbeat': {'$exists': True}})[0].get('heartbeat'))

@app.route('/periods/<period_name>/candlesticks/')
def get_candlesticks(period_name):
	ret = client.periods.find({'period_name': period_name}, {'_id': False}).sort('time', -1)
	ret_list = []
	for doc in ret:
		ret_list.append(doc)
	return jsonify(ret_list)