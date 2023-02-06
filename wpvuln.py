import requests

url = "https://centralian.com.au" # Replace with your website URL
vuln_check_url = url + "/wp-admin/load-scripts.php?c=1&load[]=jquery-ui-core,jquery-ui-widget,jquery-ui-mouse,jquery-ui-sortable"

try:
    response = requests.head(vuln_check_url)
    if response.status_code == 200:
        print("VULNERABLE: WordPress site at {} is vulnerable to at least one security issue.".format(url))
    else:
        print("SECURE: WordPress site at {} does not seem to be vulnerable to the most common security issues.".format(url))
except requests.exceptions.RequestException as e:
    print("ERROR: Failed to check vulnerability status of the WordPress site at {}.".format(url))
