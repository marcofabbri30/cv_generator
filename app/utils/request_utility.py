from fastapi import Request


warranty = '/print/warranty'

class RequestUtility:
    
    def __init__(self)->None:
        pass

    @staticmethod
    def get_base_url(request: Request):
        port = ":" + str(request.url.port) if request.url.port is not None else ""
        return request.url.scheme + "://" + request.url.hostname + port

    @staticmethod
    def get_warranty_url(request: Request, username: str, anno: int, tipo: str, nro: int, riga: int, lingua: str) -> str:
        return RequestUtility.get_base_url() + warranty + f"?username={username}&lingua={lingua}&anno={anno}&tipo={tipo}&nro={nro}&riga={riga}"

    @staticmethod
    def get_temp_base_url(request: Request):
        base_url = RequestUtility.get_base_url(request)
        return base_url + "/temp/"

    @staticmethod
    def get_static_base_url(request: Request):
        base_url = RequestUtility.get_base_url(request)
        return base_url + "/static/"

    @staticmethod
    def get_static_style_base_url(request: Request):
        base_url = RequestUtility.get_base_url(request)
        return base_url + "/static/style/"    


