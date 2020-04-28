from donor.models import BloodDonor
import fbchat
from getpass import getpass
import re
import json

def fb_notifier(request):
    donor_id = request.POST.get("donor_id")
    print("donor id ", donor_id)
    donor_profile = BloodDonor.objects.get(id=donor_id).fb_url
    print(donor_profile)
    #user = re.findall("(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?",donor_profile)
    try:
        user = donor_profile
        cookies = {}
        try:
            # Load the session cookies
            with open('session.json', 'r') as f:
                cookies = json.load(f)
        except:
            # If it fails, never mind, we'll just login again
            pass

        # Attempt a login with the session, and if it fails, just use the email & password
        client = fbchat.Client('username', 'password', session_cookies=cookies)


        friends = client.searchForUsers(user)  # return a list of names
        friend = friends[0]
        print(friends)

        # msg = str(raw_input("Message: "))
        msg = ("Hello this is a message from automated script , ami tor rokto khabo")
        # sent = client.send(friend.uid, msg)
        sent = client.sendMessage(msg, thread_id=friend.uid)
        if sent:
            print("Message sent successfully!")

        with open('session.json', 'w') as f:
            json.dump(client.getSession(), f)
    except Exception as e:
        print(e)


    return None