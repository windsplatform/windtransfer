#!/usr/bin/python3
#-*-coding:utf-8-*-
import requests
import json


def sendWind(apikey, amount, message, sender,recipient):

    url ="http://144.91.84.27:6869/transactions/sign/" + sender
    headers = {"Content-Type": "application/json", "Accept": "application/json", "X-API-Key": apikey}
    data = {"type": 4, "sender": sender, "recipient": recipient, "amount": amount, "fee": 100000, "attachment": message}
    data = json.dumps(data)
    
    r = requests.post(url, data= data, headers=headers)
    r=r.text
    r =json.loads(r)





    
    senderPublicKey = r["senderPublicKey"]
    signature = r["signature"]
    proofs = r["proofs"]
    idd = r["id"]
    timestamp = r["timestamp"]
    assetId = r['assetId']
    feeAsset = r['feeAsset']
    feeAssetId = r['feeAssetId']
    url ='http://144.91.84.27:6869/transactions/broadcast'
    data = {"senderPublicKey": senderPublicKey,"amount": amount,"signature": signature,"fee": 100000,"type": 4,"version": 1,"attachment": message,"sender": sender,"feeAssetId": feeAssetId,"proofs": proofs,"assetId": assetId,"recipient":recipient,"feeAsset":feeAsset ,"id": idd,"timestamp": timestamp}
    data = json.dumps(data)
    r1 = requests.post(url, data= data, headers=headers) 
  


