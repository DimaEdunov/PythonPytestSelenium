# This class will make our lives easier once running test suites
import os
from src.parameters import domains

"""Run tests """

suite = "dev"
domain = "av"
attraction = "xt"
opsui_site_code = domains.get_site_code(domain)
domain_cart = "ty"
attraction_cart = "br"
opsui_site_code_cart = domains.get_site_code(domain_cart)


os.system(f'pytest -v -s --alluredir="C:\\AllureReports\\Data" --html=report.html --developer=dima --self-contained-html -m={suite} --env=test --domain={domain} --domain_cart={domain_cart} --attraction={attraction} --attraction_cart={attraction_cart} --site_code={opsui_site_code} --site_code_cart={opsui_site_code_cart} --from_to_api_time_buffer_seconds=130 --headless=False')


# --dist=loadfile -n=4


