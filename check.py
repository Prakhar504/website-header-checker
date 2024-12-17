import requests

def check_headers(url):
    good_headers = [
        'Strict-Transport-Security',
        'X-Content-Type-Options',
        'X-Frame-Options',
        'X-XSS-Protection',
        'Content-Security-Policy',
        'Referrer-Policy',
        'Feature-Policy'
    ]

    bad_headers = [
        'X-Powered-By',
        'Server',
        'Access-Control-Allow-Origin'
    ]

    result = {
        'good_headers': [],
        'missing_good_headers': [],
        'bad_headers': [],
        'found_bad_headers': [],
        'https_status': ''
    }
    
    try:
        response = requests.get(url)
        headers = response.headers
        
        for header in good_headers:
            if header in headers:
                result['good_headers'].append(f"{header}: {headers[header]}")
            else:
                result['missing_good_headers'].append(f"{header}: Missing")
        
        for header in bad_headers:
            if header in headers:
                result['found_bad_headers'].append(f"{header}: {headers[header]}")
            else:
                result['bad_headers'].append(f"{header}: Not Found")
    
        if 'Strict-Transport-Security' in headers:
            result['https_status'] = "HTTPS is enforced with Strict-Transport-Security."
        else:
            result['https_status'] = "No Strict-Transport-Security header found. HTTPS may not be enforced."
    
    except requests.exceptions.RequestException as e:
        result['error'] = f"Error fetching URL: {e}"
    
    return result
