from pymongo import MongoClient
import os

def mongoCollection(connstr, db, collection):
    client = MongoClient(connstr)
    db = client[db]
    return db[collection]


def main(event, context):
    print(os.environ.get('MONGODB_CONN_STR'))
    collection = mongoCollection(os.environ.get('MONGODB_CONN_STR'), 'smsinfo', 'transactions')

    for _item in list(
    enumerate(
        collection.find({
            "message.text": {'$regex': 'ALERT: You\'ve spent Rs.([0-9.]+)'}
            }).sort([("message.date",1)]))):
        print("message", _item[1])

if __name__ == "__main__":
    main('', '')