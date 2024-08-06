import requests

def get_clan_info(tag):
    base_url = "https://api.clashofclans.com/v1/clans/"  
    url = f"{base_url}{tag}"
    headers = {"Accept": "application/json", "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijc2NWQ4NmY5LWJlMzUtNDc0My05OTJiLWM0ODMzZWFjMDAxYiIsImlhdCI6MTcyMjg2NzI1MCwic3ViIjoiZGV2ZWxvcGVyLzVlZmE4ZmFhLTBhNGUtYjc3NS1jMWZmLTAyZmRmZDljZTk1NSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjg5LjIzMi43Ny4xMzgiXSwidHlwZSI6ImNsaWVudCJ9XX0.p-_yz6JBYfsAPXOU-QFW4VpOVOvYo5tlRbItzKCKX8ArIv5EBRTi4GSPBo8fvi68J_bFJIExrY6UBeAPUK3lvQ"}

    response = requests.get(url, headers=headers)

    response.raise_for_status()  # This will raise an exception if the response status is not 200
    return response.json()

if __name__ == "__main__":
    tag = "%232G8GJGYCL"
    clan_info = get_clan_info(tag)
    print(clan_info)

