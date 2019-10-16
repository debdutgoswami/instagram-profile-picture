def user_url():
    """this fuction is used to take the username as input,
        then generate the profile url

    Returns:
        [string] -- [profile url]
    """

    username = input("enter the username - ")
    url = "https://www.instagram.com/{}/".format(username)

    return url