from pyutil.datetime_jp import now
from pyutil.http_request import requestGet

if __name__ == "__main__":
    print(f"******************* SAMPLE START : {now()} *******************")
    res = requestGet("https://google.com")
    print(res)
    print(f"******************* SAMPLE END : {now()} *******************")
