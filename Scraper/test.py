from Scraper.database import database
import datetime

def get_urls(con) -> list:
        res = con.cur.execute("select link from number limit 5")
        links = []
        for i in res.fetchall():
            links.append(i[0])
        return links

def ago_to_datetime(ago_str):
    parsed_s = ago_str.split()[:2]
    time_dict = {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}
    if len(parsed_s) == 2:
        for amount, fmt in parsed_s:
            time_dict[fmt] = float(amount)
    else:
        # Handle cases where only one value (e.g., "3 days ago") is provided
        time_dict["days"] = float(parsed_s[0])
    dt = datetime.timedelta(**time_dict)
    past_time = datetime.datetime.now() - dt
    return past_time

if __name__ == "__main__":
    # db = database("db.sqlite3")
    # print(get_urls(db))
    print(ago_to_datetime("5 days ago"))