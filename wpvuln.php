$url = "https://centralian.com.au" # Replace with your website URL
$vuln_check_url = "$url/wp-admin/load-scripts.php?c=1&load[]=jquery-ui-core,jquery-ui-widget,jquery-ui-mouse,jquery-ui-sortable"

try {
    $response = Invoke-WebRequest -Uri $vuln_check_url -Method HEAD
    if ($response.StatusCode -eq 200) {
        Write-Host "VULNERABLE: WordPress site at $url is vulnerable to at least one security issue."
    } else {
        Write-Host "SECURE: WordPress site at $url does not seem to be vulnerable to the most common security issues."
    }
} catch {
    Write-Host "ERROR: Failed to check vulnerability status of the WordPress site at $url."
}
