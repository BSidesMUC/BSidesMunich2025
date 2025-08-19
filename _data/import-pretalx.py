#env python3

import os
import json

import frontmatter
from slugify import slugify

import datetime
import dateutil.parser
from pytz import timezone

from pprint import pprint
import mimetypes
import requests

from datetime import datetime

from os import environ
access_token_key = environ.get('ACCESS_TOKEN_KEY')

HEADERS = {'Authorization': f'Token {access_token_key}'}

bsides_event = "bsides-munich-2025"

def logging():
    import logging

    # These two lines enable debugging at httplib level (requests->urllib3->http.client)
    # You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
    # The only thing missing will be the response.body which is not logged.
    try:
        import http.client as http_client
    except ImportError:
        # Python 2
        import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1

    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

def get_speaker_image(speaker):
    filepath = ''

    if speaker['avatar_url'].strip():
        with requests.Session() as s:

            res = s.get(speaker['avatar_url'], stream=True)
  
            if res.status_code == 200:
                content_type = res.headers['content-type']
                ext = mimetypes.guess_extension(content_type)
                filepath = f"img/speakers/{speaker['code']}{ext}"
                
                with open(f"{filepath}", "wb") as ifile:
                    for chunk in res:
                        ifile.write(chunk)

    return filepath

def main():

    #logging()

    today = datetime.today().strftime('%Y-%m-%d')
    event = bsides_event # The current conference slug

    with requests.Session() as s:
        s.headers = HEADERS

        # Quick check to test if the token is working
        res = s.get(f'https://pretalx.com/api/events/{event}/')
        jdata = res.json()
        
        if res.status_code == 401:
            print('401 - {}'.format(jdata['detail']))
            return
        
        # Read sessions.
        sessions = None
        filename = f'_data/{today}_sessions.json'
        if os.path.isfile(filename):
            print(f"Loading sessions from {filename} ... ", end="")
            with open(filename, 'r', encoding="utf8") as infile:
                sessions = json.load(infile)
        else:
            print("Loading sessions from Pretalx API ...", end="")
            res = s.get(f'https://pretalx.com/api/events/{event}/submissions?expand=speakers,track,submission_type,slots.room')
            jdata = res.json()
            jdata_sessions = jdata['results']
            
            while 'next' in jdata and jdata['next'] is not None:
                print(".", end="")
                res = s.get(jdata['next'])
                jdata = res.json()               
                jdata_sessions = jdata_sessions + jdata['results']

            sessions_filtered = []

            # Keep only the ones in accepted or confirmed states with an assigned room.
            for session in jdata_sessions:
                if not session['slots']:
                    continue
                elif session['state'] in ['accepted', 'confirmed']:
                    sessions_filtered.append(session)
                elif session['state'] in ['rejected', 'submitted', 'withdrawn', 'canceled']:
                    continue
                else:
                    pprint(session['state'] )
                    print("[!] Check session state")
                    input()
   
            with open(filename, 'w', encoding="utf8") as outfile:
                json.dump(sessions_filtered, outfile, indent=4, sort_keys=True)
                sessions = sessions_filtered

    print(f" loaded {len(sessions)} sessions.")

    # get session speaker photos
    speaker_photos = {}

    for session in sessions:
        for speaker in session['speakers']:
            if speaker['code'] in speaker_photos:
                pass
            else:
                filepath = get_speaker_image(speaker)
                speaker_photos[speaker['code']] = filepath

    # sort sessions and generate files.
    track_cnt = {}

    sessions_sorted = sorted(sessions, key=lambda d: d['slots'][-1]['start']) 
    for session in sessions_sorted:
        print(session['submission_type']['name']['en'], end=": ")

        session_type = session['track']['name']['en']
        if session_type in ['Talks', 'Workshops']:
            session_type = session_type.lower()[:-1]
        else:
            print(f"[!] Unrecognized track: {session_type}")
            input()

        post = frontmatter.loads('')
        post.content = session['abstract'].replace('. ', '.\n').replace('\r\n', '\n')

        post['layout'] = session_type

        post['accepted'] = session['state'] in ['accepted', 'confirmed']
            
        post['keynote'] = session['is_featured']
        post['track'] = session['slot_count']
        post['title'] = session['title']
        post['code'] = session['code']

        post['details'] = True
    
        MUC = timezone('Europe/Berlin')        
        post['timeslot'] = {
            'start': dateutil.parser.parse(session['slots'][-1]['start']).astimezone(MUC),
            'end': dateutil.parser.parse(session['slots'][-1]['end']).astimezone(MUC),
            'duration': session['duration']
        }

        post['speakers'] = [
            {
                "name": sess_speaker["name"],
                "bio": sess_speaker['biography'],
                "photo": speaker_photos[sess_speaker['code']] or False,
                "handle": False
            } 
            for sess_speaker in session['speakers'] 
        ] 

        if session_type in ['workshop', 'talk']:
            post_folder = '_' + session_type + 's'
        else:
            post_folder = session['track']['name']['en']
            print(f"[!] Check post_folder: {post_folder}")
            input()

        session_name = session['slots'][-1]['room']['name']['en']

        ws_tracks = [
            "Hochschule München - R1.006",
            "Hochschule München - R1.007",
            "Hochschule München - R1.008",
            "Hochschule München - R0.004",
            "Hochschule München - R0.006",
            "Hochschule München - R0.007",
            "Hochschule München - R0.Foyer",
            "Hochschule München - R1.Galerie",
            
        ]
        conf_tracks = [
            "WestIn - Munich",
            "WestIn - Partenkirchen",
        ]
        post['room'] = session_name

        if session_name in ws_tracks:
            post['track'] = ws_tracks.index(session_name) + 1
        elif session_name in conf_tracks:
            post['track'] = conf_tracks.index(session_name) + 1
        else:
            print(f"[!] Check post track {session_name}")
            input()


        if post_folder not in track_cnt:
            track_cnt[post_folder] = {}

        if post['track'] not in track_cnt[post_folder]:
            track_cnt[post_folder][post['track']] = 1
        else:
            track_cnt[post_folder][post['track']] += 1

        # Sort by file name? {slot}-{talkno}_{title}.md
        session_id = track_cnt[post_folder][post['track']]
        filename = f"{post['track']:03}-{session_id:02}_{post['code']}_{slugify(post['title'])}.md"

        filepath = f'{post_folder}/{filename}'
        print(filepath)

        # Check if session exists
        with open(filepath, 'w', encoding="utf8") as fh:
            
            #print(frontmatter.dumps(post))
            fh.write(frontmatter.dumps(post))

if __name__ == '__main__':
    main()
