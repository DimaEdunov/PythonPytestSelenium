import allure
import pytz
from datetime import datetime
from dateutil import parser
from src.parameters.opsui_parameters import OpsuiAppParameters

def current_time_according_to_time_zone(time_zone):
    global time_zone_Tz
    global current_time
    global time_in_time_zone

    if time_zone == "Europe/London":
        time_zone_Tz = pytz.timezone("Europe/London")

    elif time_zone == "Europe/Amsterdam":
        time_zone_Tz = pytz.timezone("Europe/Amsterdam")

    elif time_zone == "US/Pacific":
        time_zone_Tz = pytz.timezone("US/Pacific")

    elif time_zone == "US/Eastern":
        time_zone_Tz = pytz.timezone("US/Eastern")

    elif time_zone == "America/Sao_Paulo":
        time_zone_Tz = pytz.timezone("America/Sao_Paulo")

    elif time_zone == "Europe/Belgrade":
        time_zone_Tz = pytz.timezone("Europe/Belgrade")

    elif time_zone == "CET":
        time_zone_Tz = pytz.timezone("CET")

    elif time_zone == "Israel":
        time_zone_Tz = pytz.timezone("Israel")

    elif time_zone == "Asia/Tokyo":
        time_zone_Tz = pytz.timezone("Asia/Tokyo")

    else:
        print("No time for selected time zone")

    time_in_time_zone = datetime.now(time_zone_Tz)
    current_time = parser.parse(time_in_time_zone.strftime("%H:%M"))
    return current_time


def opsui_choose_feature(domain, feature):
    if domain == "aq":
        button_text = OpsuiAppParameters.get_opsui_page_name_spanish(feature)

    else:
        button_text = OpsuiAppParameters.get_opsui_page_name_english(feature)

    return button_text
