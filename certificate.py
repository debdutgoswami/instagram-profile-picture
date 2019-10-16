import ssl

def context_ssl():
    """the following function is used to take care of the SSL certificate,
        it is not mandatory to perform this step

    Returns:
        [ssl.SSLContext] -- context
    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    return ctx