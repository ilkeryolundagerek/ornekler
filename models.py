from datetime import datetime


class EarthquakeModel:
    def __init__(self, args):
        # ['2023.05.13', '19:02:44', '38.1180', '36.5870', '5.5', '0.0', '1.2', '0.0', 'KANLIKAVAK-GOKSUN', '(KAHRAMANMARAS)', 'İlksel']
        # print(args)
        self.eventTimeStamp = datetime.strptime(f"{args[0]} {args[1]}", "%Y.%m.%d %H:%M:%S")
        self.latitude = float(args[2])
        self.longitude = float(args[3])
        self.depth = float(args[4])
        self.MD = float(args[5])
        self.ML = float(args[6])
        self.Mw = float(args[7])
        if "REVIZE01" in args:
            self.location = " ".join(args[8:-3])
            self.solution = " ".join(args[-3:])
        else:
            self.location = " ".join(args[8:-1])
            self.solution = "İlksel"

    def __repr__(self):
        return str(self.__dict__)


class IsBikeMainModel:
    '''
    "serviceCode": 0,
    "serviceDesc": "İşlem Başarılı.",
    "dataList": []
    '''

    def __init__(self, serviceCode, serviceDesc, dataList):
        self.code = serviceCode
        self.desc = serviceDesc
        self.stations = dataList


class IsBikeStationModel:
    '''
    "guid": 1,
    "istasyon_no": "1117",
    "adi": "Bostancı İDO - 2",
    "aktif": 1,
    "bos": "12",
    "dolu": "3",
    "lat": "40.952389",
    "lon": " 29.090669",
    "sonBaglanti": "2023-05-16T15:37:31.403"
    '''

    def __init__(self, guid, istasyon_no, adi, aktif, bos, dolu, lat, lon, sonBaglanti):
        self.guid = int(guid)
        self.station_no = int(istasyon_no)
        self.name = adi
        self.active = int(aktif)
        self.empty = int(bos)
        self.filled = int(dolu)
        self.latitude = float(lat)
        self.longitude = float(lon)
        self.last_connection = datetime.strptime(sonBaglanti.split(".")[0], "%Y-%m-%dT%H:%M:%S")

    def __repr__(self):
        return str(self.__dict__)
