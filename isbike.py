import requests as req
from models import IsBikeMainModel, IsBikeStationModel

#Veri Merkezi: https://data.ibb.gov.tr/

base_url = "https://api.ibb.gov.tr/"
endpoint_all = "ispark-bike/GetAllStationStatus"
endpoint_one = "ispark-bike/GetStationStatus?guid="

#
def get_all():
    res = req.get(f"{base_url}{endpoint_all}")
    json_data = res.json()
    stations = []
    code = json_data["serviceCode"]
    desc = json_data["serviceDesc"]
    for s in json_data["dataList"]:
        station = IsBikeStationModel(
            s["guid"],
            s["istasyon_no"],
            s["adi"],
            s["aktif"],
            s["bos"],
            s["dolu"],
            s["lat"],
            s["lon"],
            s["sonBaglanti"]
        )
        stations.append(station)
    data = IsBikeMainModel(code, desc, stations)
    print(data.__dict__)


get_all()


def get_one(guid):
    res = req.get(f"{base_url}{endpoint_one}{guid}")
    json_data = res.json()
    s = json_data["dataList"][0]
    code = json_data["serviceCode"]
    desc = json_data["serviceDesc"]
    station = IsBikeStationModel(
        s["guid"],
        s["istasyon_no"],
        s["adi"],
        s["aktif"],
        s["bos"],
        s["dolu"],
        s["lat"],
        s["lon"],
        s["sonBaglanti"])
    data = IsBikeMainModel(code, desc, [station])
    print(data.__dict__)


get_one(924)
